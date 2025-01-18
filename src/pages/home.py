from dash import html

def home_page():
    return html.Div([
         html.Div([html.H1("Bienvenue sur MDPOL & EMPLOI ! "),], className="bienvenue"),
         html.P("Vous trouverez ici des graphiques d'analyse décrivant l'impact sur le marché de l'emploi des politiques économiques adoptées par les 4 derniers présidents de la République Française.", className="descript"),
         html.Img(src='/assets/Ministere_travail.jpeg', className="homebackground"),

    ],className="main")
