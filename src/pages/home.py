from dash import html

def home_page():
    return html.Div([
         html.Div([html.H1("BIENVENUE SUR  MDPOL & EMPLOI"),], className="bienvenue"),
         html.P("Ici vous trouverez des graphics d'analyse decrivant l'impact sur le marché de l'emploi  des politique économique adopté par les 4 derniers presidents de la republique française", className="descript"),
         html.Img(src='/assets/home.png', className="homebackground"),

    ],className="main")
