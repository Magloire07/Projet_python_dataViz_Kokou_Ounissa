
from dash import html
def description_page():

    # Lecture du fichier texte
    file_path = "assets/description.txt"
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Création du layout Dash
    return html.Div([
        html.H1("DESCRIPTION DES CATÉGORIES ", style={"textAlign": "center","color":"#30495a"}),
        html.Div([
            html.P(line, style={"whiteSpace": "pre-wrap", "margin": "5px 0"}) for line in lines
        ], style={"padding": "20px", "fontFamily": "Arial, sans-serif"},className="infopage")
    ])

