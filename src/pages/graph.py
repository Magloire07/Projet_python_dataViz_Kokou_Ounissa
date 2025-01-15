import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output, Dash
import os

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
        html.H1("Visualisez et analysez", style={"text-align": "center", "margin-bottom": 40, "color":"#142E7B"}),
        html.Div([
        # Premier groupe pour le premier graphique
        html.Div([
        html.Fieldset([ html.Legend( f"{non_empty_directories[0]}",className="legend1"),
        dcc.Dropdown(
            id="graph1-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "50%", "margin": "auto", "margin-bottom": 40}
        ),
        dcc.Graph(id="dynamic-graph1"),
        html.P("Catégories pour Graphique 1", style={"text-align": "center"}),
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
        ),
        html.P("commentaire",className="comment"),
        html.Textarea( "En cinq ans le chômage est passé de 9,5% de la population active à 7,4%, avec un mandat toujours encours ",className="textArea"),
        ]),
        ],className="graphe_frame"),
        # Deuxième groupe pour le deuxième graphique
        html.Div([
        html.Fieldset([ html.Legend( f"{non_empty_directories[1]}",className="legend1"),
        #html.H1(f"-------------{non_empty_directories[1]}-------------"),
        dcc.Dropdown(
            id="graph2-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "50%", "margin": "auto", "margin-bottom": 40}
        ),
        dcc.Graph(id="dynamic-graph2"),
        html.P("Catégories pour Graphique 2", style={"text-align": "center"}),
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
        ),
        html.P("commentaire",className="comment"),
        html.Textarea( "Confronté à la crise des subprimes, le mandat de Nicolas Sarkozy a vu le chômage passer de 8,1 à 9,5% de la population active",className="textArea"),


        ]),
        ],className="graphe_frame"),

        # Troisième groupe pour le troisième graphique
        html.Div([
        html.Fieldset([ html.Legend( f"{non_empty_directories[2]}",className="legend1"),
        dcc.Dropdown(
            id="graph3-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "50%", "margin": "auto", "margin-bottom": 40}
        ),
        dcc.Graph(id="dynamic-graph3"),
        html.P("Catégories pour Graphique 3", style={"text-align": "center"}),
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
            value='A',
            inline=True,
            style={"text-align": "center"}
            ),
                html.P("commentaire",className="comment"),
                html.Textarea( "Le mandat François Hollande n'aura pas donné lieu à une baisse spectaculaire",className="textArea"),


        ]),
        ],className="graphe_frame"),
        # Quatrième groupe pour le quatrième graphique
        html.Div([
        html.Fieldset([ html.Legend( f"{non_empty_directories[3]}",className="legend1"),
        dcc.Dropdown(
            id="graph4-selector",
            options=[
                {"label": "Histogramme", "value": "histogram"},
                {"label": "Courbe", "value": "line"}
            ],
            value="histogram",
            clearable=False,
            style={"width": "50%", "margin": "auto", "margin-bottom": 40}
        ),
        dcc.Graph(id="dynamic-graph4"),
        html.P("Catégories pour Graphique 4", style={"text-align": "center"}),
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
        ),
            html.P("commentaire",className="comment"),
             html.Textarea("La France connaît au début du quinquennat Chirac un taux de chômage supérieur à 10%. La baisse entamée en 1998 se poursuit durant la cohabitation et passe sous la barre des 8% en 2001", className="textArea"),


        ],className="graphe_frame")
           ])
        ],className="graphs")
    ])
# Callback pour mettre à jour chaque graphique individuellement
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
                fig = px.bar(data, x="periodes", y="nombre_demandeur_emploi", title=f"Histogramme {i}", height=450)
                fig.update_traces(marker_color=color[i-1])

            else:
                fig = px.line(data, x="periodes", y="nombre_demandeur_emploi", title=f"Courbe {i}", height=450)
            fig.update_layout(
                xaxis_title="Période",
                yaxis_title="Nombre de demandeurs d'emploi",
                template="plotly_white"
            )
            return fig
# Initialisation de l'application Dash
app = Dash(__name__)
app.layout = graph_page()
register_callbacks(app)
if __name__ == "__main__":
    app.run_server(debug=True)
