import json
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html,Input, Output

with open("assets/DeptsName.txt", "r", encoding="utf-8") as file:
    depts = file.read().splitlines()

mandats = {
    "Chirac 1995-2002": (1995, 2002),
    "Chirac 2002-2007": (2002, 2007),
    "Sarkozy 2007-2012": (2007, 2012),
    "Hollande 2012-2017": (2012, 2017),
    "Macron 2017-2022": (2017, 2022),
    "Macron 2022-2025":(2022, 2025)
}

def load_data():
    all_data = []
    for dep_name in depts:  # Utiliser les noms des départements
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
    # convertir les données collectées en DataFrame
    df = pd.DataFrame(all_data)
    return df



# cartes Plotly pour chaque mandat
def create_figures():

    # Charger les données
    df = load_data()

    # Calculer la moyenne de chômage par mandat et par département
    mandat_data = []
    for mandat, (start, end) in mandats.items():
        mandat_df = df[(df["annee"] >= start) & (df["annee"] <= end)]
        
        # Grouper les données par code de département et calculer la moyenne du nombre de demandeurs d'emploi
        avg_data = mandat_df.groupby("code_departement")["nombre_demandeur_emploi"].mean().reset_index()
        
        # Ajouter le nom du département à chaque ligne 
        avg_data["mandat"] = mandat
        
        # Récupérer le nom du département pour chaque code_departement en utilisant 'merge'
        avg_data = avg_data.merge(mandat_df[["code_departement", "nom_departement"]].drop_duplicates(), on="code_departement", how="left")
        
        mandat_data.append(avg_data)

    final_df = pd.concat(mandat_data)



    with open("assets/departements.json", "r", encoding="utf-8") as file:
        france_departments = json.load(file)
    figures = []
    for mandat in mandats:
        mandat_df = final_df[final_df["mandat"] == mandat]
        if mandat_df.empty:  # Si les données sont vides, on saute ce mandat
            continue
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
            title=f"Nbr de chômeurs moyen par département ({mandat})",
            hover_name="nom_departement",  # Affiche le nom du département dans le popup
            hover_data={"nombre_demandeur_emploi": True, "mandat": False},  # Affiche le taux de chômage, mais pas le mandat
        )
        fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})
        figures.append(fig)

    return figures
# Fonction pour créer la page avec Dash


def register_callbacks5(app):
    for i in range(6):
        @app.callback(
                Output(f"graph{i}", "figure"),
                [Input(f"graph{i}", "id")], 
        )
        def update_graph(_,i=i):
            figures = create_figures()
            return figures[i]
        


def map_page():
    return html.Div([
        html.H1("Évolution du chômage par mandat présidentiel", className="title"),
        html.Div([
            dcc.Graph( className="map-graph", id="graph0"),
            dcc.Graph( className="map-graph", id="graph1"),
            dcc.Graph( className="map-graph", id="graph2"),
            dcc.Graph( className="map-graph", id="graph3"),
            dcc.Graph( className="map-graph", id="graph4"),
            dcc.Graph( className="map-graph", id="graph5"),
        ], className="maps-container")
    ])
