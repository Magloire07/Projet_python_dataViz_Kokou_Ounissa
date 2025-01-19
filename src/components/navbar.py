from dash import html

def navbar():
    return html.Nav([
         html.Img(src='/assets/logo.png',style={"width":110, "margin-left":20}),

        html.Ul([
            html.Li(html.A("Accueil", href="/")),
            html.Li(html.A("Données par mandats", href="/graphs")),
            html.Li(html.A("Données par régions", href="/regions")),
            html.Li(html.A("Carte", href="/map")),
            html.Li(html.A("Informations", href="/description")),


        ], className="nav-list"),
    ], className="navbar")
