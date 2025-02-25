import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, Dash
import plotly.graph_objects as go
import os
import json

def get_non_empty_dirs(directory):
    # Liste pour stocker les noms des répertoires non vides
    non_empty_dirs = []
    
    try:
        # Vérifie si le répertoire existe
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Le répertoire '{directory}' n'existe pas.")
        
        # Parcourt les sous-répertoires
        for subdir in os.listdir(directory):
            full_path = os.path.join(directory, subdir)
            # Vérifie si c'est un répertoire et s'il contient des fichiers ou sous-répertoires
            if os.path.isdir(full_path) and os.listdir(full_path):
                non_empty_dirs.append(subdir)
    
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    
    return non_empty_dirs

cleaned_dir = "data/cleaned"
non_empty_directories = get_non_empty_dirs(cleaned_dir)
color=["rgb(128, 181, 254)","rgb(255, 128, 189)","rgb(255, 152, 16)","rgb(27, 102, 152)"]
# Fonction pour créer un layout de page dynamique




def graph_page():

    return html.Div([
        html.Div([
            #options
        html.Div([
             html.H2("DEDUCTION", style={"text-align": "center", "margin-bottom": 20,"color":"#30495a"}),
             html.H3("Emmanuel Macron", style={"text-align": "center", "margin-bottom": 20}),
             html.P( "En cinq ans le chômage est passé de 9,5% de la population active à 7,4%, avec un mandat toujours encours ",className="com"),
             html.H3("Nicolas Sarkozy", style={"text-align": "center", "margin-bottom": 20}),
             html.P( "Confronté à la crise des subprimes, le mandat de Nicolas Sarkozy a vu le chômage passer de 8,1 à 9,5% de la population active",className="com"),
             html.H3("François Hollande", style={"text-align": "center", "margin-bottom": 20}),
             html.P( "Le mandat François Hollande n'aura pas donné lieu à une baisse spectaculaire",className="com"),
             html.H3("Jacques Chirac", style={"text-align": "center", "margin-bottom": 20}),
             html.P("La France connaît au début du quinquennat Chirac un taux de chômage supérieur à 10%. La baisse entamée en 1998 se poursuit durant la cohabitation et passe sous la barre des 8% en 2001", className="com"),

        ],className="options"),

        # histogrammes
        html.Div([ 
        # Premier groupe pour le premier graphique
        html.Div([
        dcc.Graph(id="dynamic-graph1"),
        #html.P("Catégories pour Graphique 1", style={"text-align": "center"}),
        html.Div([
            dcc.Dropdown(
            id="graph1-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "150px"}
        ),
            dcc.RadioItems(
            id='radio-selector1',
            options=[
                {'label': 'A', 'value': 'A'},
                {'label': 'B', 'value': 'B'},
                {'label': 'ABC', 'value': 'ABC'},
                {'label': 'C', 'value': 'C'},
                {'label': 'D', 'value': 'D'},
                {'label': 'E', 'value': 'E'}
            ],
            value='A',
            inline=True,
            style={"text-align": "center"}
        )
        ],className="type_cat"),

        ],className="graphe_frame"),
         
        
        # Troisiemme groupe  pour le troisiemme graphique 
        html.Div([
        dcc.Graph(id="dynamic-graph3"),
        html.Div([
            dcc.Dropdown(
            id="graph3-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="line",
            clearable=False,
            style={"width": "150px"}
        ),
            dcc.RadioItems(
            id='radio-selector3',
            options=[
                {'label': 'A', 'value': 'A'},
                {'label': 'B', 'value': 'B'},
                {'label': 'ABC', 'value': 'ABC'},
                {'label': 'C', 'value': 'C'},
                {'label': 'D', 'value': 'D'},
                {'label': 'E', 'value': 'E'}
            ],
            value='E',
            inline=True,
            style={"text-align": "center"}
        )
        ],className="type_cat"),
        ],className="graphe_frame"),
                 

        # Deuxième groupe pour le deuxième graphique
        html.Div([
        dcc.Graph(id="dynamic-graph2"),
        html.Div([
            dcc.Dropdown(
            id="graph2-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "150px"}
        ),
            dcc.RadioItems(
            id='radio-selector2',
            options=[
                {'label': 'A', 'value': 'A'},
                {'label': 'B', 'value': 'B'},
                {'label': 'ABC', 'value': 'ABC'},
                {'label': 'C', 'value': 'C'},
                {'label': 'D', 'value': 'D'},
                {'label': 'E', 'value': 'E'}
            ],
            value='A',
            inline=True,
            style={"text-align": "center"}
        )
        ],className="type_cat"),

        ],className="graphe_frame"),

        # Quatriemme groupe pour le quatriemme graphique 
        html.Div([
        dcc.Graph(id="dynamic-graph4"),
        html.Div([
            dcc.Dropdown(
            id="graph4-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "150px"}
        ),
            dcc.RadioItems(
            id='radio-selector4',
            options=[
                {'label': 'A', 'value': 'A'},
                {'label': 'B', 'value': 'B'},
                {'label': 'ABC', 'value': 'ABC'},
                {'label': 'C', 'value': 'C'},
                {'label': 'D', 'value': 'D'},
                {'label': 'E', 'value': 'E'}
            ],
            value='A',
            inline=True,
            style={"text-align": "center"}
        )
        ],className="type_cat"),

        ],className="graphe_frame")
         ],className="chart_scroll"),

           #donut 
        html.Div([
            html.Div([
            dcc.Graph(className="pie", id="donut01")
            ],className="donut1"),
            html.Div([
            dcc.Graph(className="pie", id="donut02")
            ],className="donut2")
            
        ],className="donuts"),
      ],className="graphs")
    ])
# Callback pour mettre à jour chaque graphique individuellement

def register_callbacks3(app):
        @app.callback(
            Output(f"donut01", "figure"),
            [
                Input("graph1-selector", "value")
            ]
        )
        def update_graph(_):
            data = pd.read_json(f"data/cleaned/coupleCodeDeptEtTauxChomage.json")
            # Calculer et ajout de la colonne la taux
            somme = sum(data["nombre_chomeurs"])
            data['taux'] = data["nombre_chomeurs"].apply(lambda x: (x * 100) / somme)

            # Appliquer un seuil pour regrouper les petites valeurs
            seuil = 1.8  # Pourcentage minimum pour afficher un département
            autres = data[data['taux'] < seuil]['taux'].sum()
            
            # Filtrer les labels et valeurs
            labels_filtrés = data[data['taux'] >= seuil]['code_dept'].tolist() # ici code_dept est le nom du departement 
            #labels_filtrés.append("Autres")
            
            valeurs_filtrées = data[data['taux'] >= seuil]['taux'].tolist()
            #valeurs_filtrées.append(autres)

            # Créer la figure
            fig1 = go.Figure()
            fig1.add_trace(
            go.Pie(
                labels=labels_filtrés,
                values=valeurs_filtrées,
                name="Taux",
                hole=0.6,
                textinfo="label+percent",
                #pull=[0 if label == "Autres" else 0.5 for label in labels_filtrés]
            )
        )
            fig1.update_layout(
                title_text="Proportion demandeurs d'emploi (1996-2023), catégorie A et  semestre4",
                annotations=[dict(text="PDE", x=0.5, y=0.5, font_size=20, showarrow=False)],
                showlegend=True
            )
            return fig1


#donut2
def register_callbacks4(app):
    @app.callback(
        Output("donut02", "figure"),
        [
            Input("graph1-selector", "value")
        ]
    )
    def update_graph(_):
        # Charger les données
        data = pd.read_json(f"data/cleaned/coupleCodeDeptEtPopMoy.json")
        with open(f"assets/coupleDeptCode.json", "r") as f:
            coupleDeptCode = json.load(f)

        # Calculer et ajout de la colonne la densité
        somme = sum(data["population_moy"])
        data['densite'] = data["population_moy"].apply(lambda x: (x * 100) / somme)

        # Appliquer un seuil pour regrouper les petites valeurs
        seuil = 2  # Pourcentage minimum pour afficher un département
        autres = data[data['densite'] < seuil]['densite'].sum()
        
        # Filtrer les labels et valeurs
        labels_filtrés = data[data['densite'] >= seuil]['code_dept'].tolist()
        labels_filtrés.append("Autres")
        
        valeurs_filtrées = data[data['densite'] >= seuil]['densite'].tolist()
        valeurs_filtrées.append(autres)

        labels_filtrés = [coupleDeptCode.get(code, code) for code in labels_filtrés]  # Remplace avec le nom du département ou "Autres"

        # Créer la figure
        fig2 = go.Figure()
        fig2.add_trace(
            go.Pie(
                labels=labels_filtrés,
                values=valeurs_filtrées,
                name="Densité",
                hole=0.6,
                textinfo="label+percent",
               # pull=[0.1 if label == "Autres" else 0 for label in labels_filtrés]
            )
        )
        fig2.update_layout(
            title_text="Densité population par département",
            annotations=[dict(text="DAP", x=0.5, y=0.5, font_size=10, showarrow=False)],
            showlegend=True,
        )
        return fig2

        

def register_callbacks(app):
    for i in range(1, 5):
        @app.callback(
            Output(f"dynamic-graph{i}", "figure"),
            [
                Input(f"graph{i}-selector", "value"),
                Input(f'radio-selector{i}', 'value')
            ]
        )
        def update_graph(graph_type , categorie,i=i):
            data = pd.read_json(f"data/cleaned/{non_empty_directories[i-1]}/listSommecat_{categorie}.json")
            if graph_type == "histogram":
                fig = px.bar(data, x="periodes", y="nombre_demandeur_emploi", title=f"{non_empty_directories[i-1]}", height=400)
                fig.update_traces(marker_color=color[i-1])

            else:
                fig = px.line(data, x="periodes", y="nombre_demandeur_emploi", title=f"{non_empty_directories[i-1]}", height=400)
                fig.update_traces(line_color=color[i-1])

            fig.update_layout(
                xaxis_title="Période",
                yaxis_title="Nombre de demandeurs d'emploi",
                template="plotly_white"
            )
            return fig

