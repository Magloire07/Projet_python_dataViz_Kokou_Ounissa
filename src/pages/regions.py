import pandas as pd
import os
import json
import plotly.express as px
from dash import dcc, html, Input, Output, Dash

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
    departements = chomage_data['Nom Officiel Département'].unique()
    writeDeptName(departements)

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

        # ecrit de fichier de couple code département et taux chomage 
    tauxByDept()


def get_non_empty_dirs(directory):
    non_empty_dirs = []
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Le répertoire '{directory}' est introuvable.")
        for subdir in os.listdir(directory):
            full_path = os.path.join(directory, subdir)
            if os.path.isdir(full_path) and os.listdir(full_path):
                non_empty_dirs.append(subdir)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    return non_empty_dirs

# Dictionnaire des années de mandats
mandats = {
    "Jacques Chirac": (1995, 2007),
    "Nicolas Sarkozy": (2007, 2012),
    "François Hollande": (2012, 2017),
    "Emmanuel Macron": (2017, 2025)
}

# Dictionnaire des couleurs par mandat présidentiel
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
    file_path = 'data/raw/labouref-france-departement-quarter-jobseeker.csv'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Le fichier {file_path} est introuvable.")
    chomage_data = pd.read_csv(file_path, delimiter=';')

    return html.Div([
        html.H1("Analyse des Chiffres du Chômage par Département selon le Mandat Présidentiel", style={"text-align": "center"}),
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
                value="line",
                style={"text-align": "center", "margin-bottom": "20px"}
            ),
            dcc.Graph(id="dynamic-graph")
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
        data = pd.read_json(data_path)
        
        # Agréger les données par année en calculant la moyenne des demandeurs d'emploi
        data_aggregated = data.groupby('annee').agg({'nombre_demandeur_emploi': 'mean'}).reset_index()

        # Créer un graphique avec les données agrégées
        if graph_type == "bar":
            fig = px.bar(data_aggregated, x="annee", y="nombre_demandeur_emploi", title=f"Chômage - {departement}", height=400)
        else:
            fig = px.line(data_aggregated, x="annee", y="nombre_demandeur_emploi", title=f"Chômage - {departement}", height=400)

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
            annotations=[
                dict(
                    x=0.95, y=0.95, xref="paper", yref="paper",
                    text="Mandat Présidentiels", showarrow=False, font=dict(size=14),
                    align="center", bgcolor="rgba(255, 255, 255, 0.7)", borderpad=10
                ),
                dict(
                    x=0.95, y=0.9, xref="paper", yref="paper",
                    text="Chirac: rouge, Sarkozy: orange, Hollande: bleu, Macron: vert",
                    showarrow=False, font=dict(size=12),
                    align="center", bgcolor="rgba(255, 255, 255, 0.7)", borderpad=10
                )
            ]
        )

        return fig



def writeDeptName(departements):
    print(f"Création:   DeptsName.txt ")
    with open("data/cleaned/DeptsName.txt", "a", encoding="utf-8") as file:
        for nom in departements:
            file.write(nom + "\n")


def tauxByDept():
    listDept=[]
    listTaux=[]
    with open("data/cleaned/DeptsName.txt", "r") as fichier:
        for ligne in fichier:
            listDept.append(ligne.strip())
    for dept in listDept:
        with open(f"data/cleaned/{dept}.json", "r") as f:
            dept_data = json.load(f)        
        somme= sum(demandeur_par_annee["nombre_demandeur_emploi"]  for demandeur_par_annee in dept_data)
        listTaux.append(somme)
        
    dico_by_cat= {"code_dept":listDept, "nombre_chomeurs":listTaux }
    print(f"Création:   coupleCodeDeptEtTauxChomage.json ")
    with open(f"data/cleaned/coupleCodeDeptEtTauxChomage.json","w") as file:
        json.dump(dico_by_cat, file, indent=4, ensure_ascii=False)