import pandas as pd
import os
import json
import plotly.express as px
from dash import dcc, html, Input, Output, Dash

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
departements = chomage_data['Nom Officiel Département'].unique()

# Itérer sur chaque département pour générer des fichiers JSON
for departement in departements:
    # Filtrer les données pour le département
    data_filtered = chomage_data[chomage_data['Nom Officiel Département'] == departement]
    # Créer une structure de données pour JSON
    data_json = []
    for _, row in data_filtered.iterrows():
        data_json.append({
            "periodes": row['Période (Trimestre)'],
            "nombre_demandeur_emploi": row['Nb moyen demandeur emploi'],
            "code_departement": row['Code Officiel Département'],
            "nom_departement": row['Nom Officiel Département'],
            "annee": row['Année']
        })
    # Créer le chemin du fichier JSON pour chaque département
    json_filename = f"{departement}.json"
    json_filepath = os.path.join(output_dir, json_filename)
    # Sauvegarder les données filtrées dans un fichier JSON
    with open(json_filepath, 'w') as json_file:
        json.dump(data_json, json_file, indent=4)

    print(f"Fichier généré : {json_filepath}")

# Initialisation Dash
app = Dash(__name__)

# Page des régions
def regions_page():
    return html.Div([
        html.H1("Analyse des Chiffres du Chômage par Mandat Présidentiel", style={"text-align": "center"}),
        html.Div([
            dcc.Dropdown(
                id="department-selector",
                options=[{"label": dep, "value": dep} for dep in chomage_data['Nom Officiel Département'].unique()],
                value=chomage_data['Nom Officiel Département'].iloc[0],
                clearable=False,
                style={"width": "60%", "margin": "auto", "margin-bottom": "20px"}
            ),
            dcc.RadioItems(
                id="graph-type-selector",
                options=[
                    {"label": "Histogramme", "value": "bar"},
                    {"label": "Courbe", "value": "line"}
                ],
                value="bar",
                style={"text-align": "center", "margin-bottom": "20px"}
            ),
            dcc.Graph(id="dynamic-graph1")
        ], style={"border": "2px solid #142E7B", "padding": "20px", "margin-bottom": "40px"})
    ])

app.layout = regions_page()

# Callback pour mettre à jour chaque graphique individuellement
def register_callbacks(app):
    @app.callback(
        Output("dynamic-graph1", "figure"),
        [Input("department-selector", "value"), Input("graph-type-selector", "value")]
    )
    def update_graph(departement, graph_type):
        # Charger les données filtrées pour le département
        data_path = f"data/cleaned/{departement}.json"
        data = pd.read_json(data_path)

        # Agrégation des données par année
        data_aggregated = data.groupby(['annee']).agg({'nombre_demandeur_emploi': 'mean'}).reset_index()

        # Créer un graphique en fonction du type
        if graph_type == "bar":
            fig = px.bar(data_aggregated, x="annee", y="nombre_demandeur_emploi", title=f"Chômage - {departement}", height=400)
        else:
            fig = px.line(data_aggregated, x="annee", y="nombre_demandeur_emploi", title=f"Chômage - {departement}", height=400)

        fig.update_layout(
            xaxis_title="Année",
            yaxis_title="Nombre de demandeurs d'emploi",
            template="plotly_white"
        )
        return fig

app.layout = regions_page()
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
