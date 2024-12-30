from dash import html

def home_page():
    return html.Div([
         html.Div([html.H1("Bienvenue sur WStatAnalyser"),   html.Img(src='/assets/analyse.png',style={"border-radius":10, "width":110, "margin-left":20}),], className="bienvenue"),
         html.P("Ici vous trouverez des graphics d'analyse sur le taux de chômage par régions de la France métropolitaine"),
         html.Img(src='/assets/france-travail.jpg',style={"border-radius":10,"height":700,"width":1600}),

    ],className="main")
