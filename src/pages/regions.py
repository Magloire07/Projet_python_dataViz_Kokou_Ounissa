import pandas as pd
import os
import json
import plotly.express as px
from dash import dcc, html, Input, Output, Dash


# Fonction pour nettoyer les données par département et sauvegarder en JSON
def readDeptName():
    listDept = []
    with open("assets/DeptsName.txt", "r") as fichier:
        for ligne in fichier:
            listDept.append(ligne.strip())
    return listDept

departements= readDeptName()

def cleanDataByDept():
    # Charger les données CSV
    file_path = 'data/raw/labouref-france-departement-quarter-jobseeker.csv'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} est introuvable.")
    chomage_data = pd.read_csv(file_path, delimiter=';')

    # Conversion de la date et extraction de l'année
    chomage_data['Date'] = pd.to_datetime(chomage_data['Date'], format='%Y-%m')
    chomage_data['Année'] = chomage_data['Date'].dt.year

    # Créer le répertoire de sortie pour les fichiers JSON
    output_dir = "data/cleaned"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Liste des départements uniques
    #departements = chomage_data['Nom Officiel Département'].unique()

    # Itérer sur chaque département pour créer un fichier JSON
    for departement in departements:
        data_filtered = chomage_data[
            (chomage_data['Nom Officiel Département'] == departement) &
            (chomage_data['Catégorie'] == 'A') &
            (chomage_data['Période (Trimestre)'].str[5:7] == 'T4')]
        data_json = []
        for _, row in data_filtered.iterrows():
            data_json.append({
                "periodes": row['Période (Trimestre)'],
                "nombre_demandeur_emploi": row['Nb moyen demandeur emploi'],
                "code_departement": row['Code Officiel Département'],
                "nom_departement": row['Nom Officiel Département'],
                "annee": row['Année']
            })
        # Sauvegarder dans un fichier JSON
        json_filename = f"{departement}.json"
        json_filepath = os.path.join(output_dir, json_filename)
        with open(json_filepath, 'w') as json_file:
            json.dump(data_json, json_file, indent=4)
        print(f"Fichier généré : {json_filepath}")

    # Créer le fichier des départements et taux de chômage
    tauxByDept()

# def writeDeptName(departements):
#     print(f"Création:   DeptsName.txt ")
#     with open("data/cleaned/DeptsName.txt", "a", encoding="utf-8") as file:
#         for nom in departements:
#             file.write(nom + "\n")



def tauxByDept():
    listDept = []
    listTaux = []
    with open("assets/DeptsName.txt", "r") as fichier:
        for ligne in fichier:
            listDept.append(ligne.strip())
    for dept in listDept:
        with open(f"data/cleaned/{dept}.json", "r") as f:
            dept_data = json.load(f)
        somme = sum(demandeur_par_annee["nombre_demandeur_emploi"] for demandeur_par_annee in dept_data)
        listTaux.append(somme)
    dico_by_cat = {"code_dept": listDept, "nombre_chomeurs": listTaux}
    print(f"Création:   coupleCodeDeptEtTauxChomage.json ")
    with open(f"data/cleaned/coupleCodeDeptEtTauxChomage.json", "w") as file:
        json.dump(dico_by_cat, file, indent=4, ensure_ascii=False)

# Dictionnaire des mandats et des couleurs
mandats = {
    "Jacques Chirac": (1995, 2007),
    "Nicolas Sarkozy": (2007, 2012),
    "François Hollande": (2012, 2017),
    "Emmanuel Macron": (2017, 2025)
}

mandat_colors = {
    "Jacques Chirac": "red",
    "Nicolas Sarkozy": "orange",
    "François Hollande": "blue",
    "Emmanuel Macron": "green"
}

# Fonction pour obtenir la couleur et la période du mandat
def get_mandat_and_color(annee):
    for mandat, (start, end) in mandats.items():
        if start <= annee <= end:
            return mandat, mandat_colors.get(mandat, "gray")
    return None, "gray"

# Initialisation Dash
app = Dash(__name__)

# Page des régions
def regions_page():
    # Charger les données CSV

    return html.Div([
        html.H1("Analyse des Chiffres du Chômage par Département selon le Mandat Présidentiel", style={"text-align": "center", "font-size": "24px"}),
        html.Div([
            dcc.Dropdown(
                id="department-selector",
                options=[{"label": dep, "value": dep} for dep in departements ],
                value=departements[0],
                clearable=False,
                style={"max-width": "55%", "margin": "auto", "margin-bottom": "20px"}
            ),
            dcc.RadioItems(
                id="graph-type-selector",
                options=[
                    {"label": "Histogramme", "value": "bar"},
                    {"label": "Courbe", "value": "line"}
                ],
                value="line",
                style={"text-align": "center", "margin-bottom": "20px"}
            ),
            dcc.Graph(id="dynamic-graph"),
            # Explication des couleurs sous le graphique
            html.Div(
                "Chirac: rouge, Sarkozy: orange, Hollande: bleu, Macron: vert",
                style={"text-align": "center", "margin-top": "20px", "font-size": "14px", "color": "black"}
            )
        ], style={"border": "2px solid #142E7B", "padding": "20px", "margin-bottom": "40px"})
    ])

app.layout = regions_page()

# Callback pour mettre à jour chaque graphique individuellement
def register_callbacks2(app):
    @app.callback(
        Output("dynamic-graph", "figure"),
        [Input("department-selector", "value"), Input("graph-type-selector", "value")]
    )
    def update_graph(departement, graph_type):
        # Charger les données filtrées pour le département
        data_path = f"data/cleaned/{departement}.json"
        try:
            data = pd.read_json(data_path)
        except Exception as e:
            print(f"Erreur lors du chargement des données : {e}")
            return {}

        # Vérifier les colonnes disponibles et ajuster
        columns_needed = ['nombre_demandeur_emploi']
        available_columns = [col for col in columns_needed if col in data.columns]

        # Si des colonnes sont manquantes, afficher un message et ne pas continuer avec l'incomplet
        if not available_columns:
            print(f"Colonnes manquantes dans les données pour {departement}: {data.columns}")
            return {}

        # Agréger les données par année
        data_aggregated = data.groupby('annee').agg({col: 'mean' for col in available_columns}).reset_index()

        # Créer un graphique avec les données agrégées
        if graph_type == "bar":
            fig = px.bar(data_aggregated, x="annee", y=available_columns,
                         title=f"Chômage - {departement}", height=400)
        else:
            fig = px.line(data_aggregated, x="annee", y=available_columns,
                          title=f"Chômage - {departement}", height=400)

        # Ajouter les bandes de couleur représentant les mandats présidentiels
        for mandat, (start, end) in mandats.items():
            color = mandat_colors.get(mandat, "gray")
            fig.add_vrect(
                x0=start, x1=end,
                fillcolor=color, opacity=0.3,
                layer="below", line_width=0
            )

        # Ajouter une légende
        fig.update_layout(
            xaxis_title="Année",
            yaxis_title="Nombre de demandeurs d'emploi",
            template="plotly_white",
            legend=dict(
                title="Mandat Présidentiels",
                x=0.5, y=-0.2,  # Position sous le graphique
                xanchor="center", yanchor="top",
                orientation="h"  # Disposition horizontale
            )
        )

        return fig

register_callbacks2(app)

# Démarrer l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
