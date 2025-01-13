import os 
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import src.components.navbar as navbar
from src.pages.home import home_page
from src.pages.graph import graph_page , register_callbacks
from src.pages.geoLoc import map_page
from src.pages.description import description_page

from src.components.footer import footer
from src.utils.get_data import  startDownload
from src.utils.clean_data import starCleaning
app = Dash(__name__, suppress_callback_exceptions=False)
app.title = "WStatAnalyser"

# Layout principal
app.layout = html.Div([
    dcc.Location(id="url"),
    navbar.navbar(),
    html.Div(id="page-content"),
    footer()
])
# Register callbacks
register_callbacks(app)

# Callbacks pour le routage
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/graphs":
        return graph_page()
    elif pathname == "/map":
        return map_page()
    elif pathname == "/description":
        return description_page()
    else:
        return home_page()
    

if __name__ == "__main__":

    app.run_server(debug=True)
