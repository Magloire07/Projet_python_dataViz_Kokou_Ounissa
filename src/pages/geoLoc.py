import json
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import os

# Charger le GeoJSON des départements
with open("data/cleaned/departements.json", "r", encoding="utf-8") as file:
    france_departments = json.load(file)

# Définir les mandats présidentiels avec leurs périodes
mandats = {
    "Chirac 1995-2002": (1995, 2002),
    "Chirac 2002-2007": (2002, 2007),
    "Sarkozy 2007-2012": (2007, 2012),
    "Hollande 2012-2017": (2012, 2017),
    "Macron 2017-2022": (2017, 2022)
}

# Charger les données de chômage depuis les fichiers JSON des départements
departements = [
    "Ain", "Aisne", "Allier", "Alpes-de-Haute-Provence", "Hautes-Alpes", "Alpes-Maritimes", 
    "Ardèche", "Ardennes", "Ariège", "Aube", "Aude", "Aveyron", "Bouches-du-Rhône", "Calvados", 
    "Cantal", "Charente", "Charente-Maritime", "Cher", "Corrèze", "Côte-d'Or", "Côtes-d'Armor", 
    "Creuse", "Dordogne", "Doubs", "Drôme", "Eure", "Eure-et-Loir", "Finistère", "Gard", 
    "Haute-Garonne", "Gers", "Gironde", "Hérault", "Ille-et-Vilaine", "Indre", "Indre-et-Loire", 
    "Isère", "Jura", "Landes", "Loir-et-Cher", "Loire", "Haute-Loire", "Loire-Atlantique", 
    "Loiret", "Lot", "Lot-et-Garonne", "Manche", "Marne", "Haute-Marne", "Mayenne", "Meurthe-et-Moselle", 
    "Meuse", "Morbihan", "Moselle", "Nièvre", "Nord", "Oise", "Orne", "Pas-de-Calais", "Puy-de-Dôme", 
    "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Pyrénées-Orientales", "Bas-Rhin", "Haut-Rhin", 
    "Rhône", "Haute-Saône", "Saône-et-Loire", "Sarthe", "Savoie", "Haute-Savoie", "Paris", 
    "Seine-Maritime", "Seine-et-Marne", "Yvelines", "Deux-Sèvres", "Somme", "Tarn", "Tarn-et-Garonne", 
    "Var", "Vaucluse", "Vendée", "Vienne", "Haute-Vienne", "Vosges", "Yonne", "Territoire de Belfort", 
    "Essonne", "Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne", "Val-d'Oise", 
    "Lozère", "Indre-et-Loire", "Haute-Corse", "Corse-du-Sud", "Maine-et-Loire"
]

def load_data():
    all_data = []
    for dep_name in departements:  # Utiliser les noms des départements
        file_path = f"data/cleaned/{dep_name}.json"
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                dep_data = json.load(f)
                # Vérifie que chaque entrée contient 'annee'
                filtered_data = [entry for entry in dep_data if "annee" in entry]
                all_data.extend(filtered_data)
        except FileNotFoundError:
            print(f"Fichier non trouvé : {file_path}")
        except json.JSONDecodeError as e:
            print(f"Erreur de parsing JSON dans {file_path} : {e}")
    # Convertir les données collectées en DataFrame
    df = pd.DataFrame(all_data)
    return df

# Charger les données
df = load_data()

# Vérifie les colonnes disponibles et affiche un aperçu des données
print("Colonnes disponibles dans df :", df.columns)
print(df.head())

# Calculer la moyenne de chômage par mandat et par département
mandat_data = []
for mandat, (start, end) in mandats.items():
    mandat_df = df[(df["annee"] >= start) & (df["annee"] <= end)]
    avg_data = mandat_df.groupby("code_departement")["nombre_demandeur_emploi"].mean().reset_index()
    avg_data["mandat"] = mandat
    avg_data["nom_departement"] = mandat_df["nom_departement"].iloc[0]  # Utiliser le nom du département
    mandat_data.append(avg_data)

final_df = pd.concat(mandat_data)

# Générer les cartes Plotly pour chaque mandat
def create_figures():
    figures = []
    for mandat in mandats:
        mandat_df = final_df[final_df["mandat"] == mandat]
        fig = px.choropleth_mapbox(
            mandat_df,
            geojson=france_departments,
            locations="code_departement",
            color="nombre_demandeur_emploi",
            featureidkey="properties.code",  # Clé pour relier le GeoJSON et les données
            mapbox_style="carto-positron",
            center={"lat": 46.603354, "lon": 1.888334},
            zoom=5,
            color_continuous_scale="Viridis",
            title=f"Taux de chômage moyen par département ({mandat})",
            hover_name="nom_departement",  # Affiche le nom du département dans le popup
            hover_data={"nombre_demandeur_emploi": True, "mandat": False},  # Affiche le taux de chômage, mais pas le mandat
        )
        fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})
        figures.append(fig)
    return figures

# Fonction pour créer la page avec Dash
def map_page():
    figures = create_figures()
    return html.Div([
        html.H1("Évolution du chômage par mandat présidentiel", style={"textAlign": "center"}),
        html.Div([
            dcc.Graph(figure=figures[0], style={"height": "50vh"}),
            dcc.Graph(figure=figures[1], style={"height": "50vh"}),
            dcc.Graph(figure=figures[2], style={"height": "50vh"}),
            dcc.Graph(figure=figures[3], style={"height": "50vh"}),
        ], style={"display": "grid", "gridTemplateColumns": "1fr", "gap": "20px"})
    ])

# Initialiser l'application Dash
app = Dash(__name__)
app.layout = map_page()

# Lancer le serveur Dash
if __name__ == "__main__":
    app.run_server(debug=True)
