from dash import html

def navbar():
    return html.Nav([
         html.Img(src='/assets/logo.png',style={"width":120, "margin-left":20}),

        html.Ul([
            html.Li(html.A("Home", href="/")),
            html.Li(html.A("Graphiques", href="/graphs")),
            html.Li(html.A("Carte", href="/map")),
            html.Li(html.A("informations", href="/description")),

        ], className="nav-list"),
    ], className="navbar")
