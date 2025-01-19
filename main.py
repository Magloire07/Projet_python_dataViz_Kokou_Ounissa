import os 
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import src.components.navbar as navbar
from src.pages.home import home_page
from src.pages.graph import graph_page , register_callbacks,register_callbacks3,register_callbacks4
from src.pages.geoLoc import map_page
from src.pages.regions import regions_page ,register_callbacks2,cleanDataByDept
from src.pages.description import description_page 
from src.components.footer import footer
from src.utils.get_data import  startDownload
from src.utils.clean_data import starCleaning
from config import host,port,debug,suppress_callback_exceptions,titre,use_reloader,use_debugger,dev_tools_ui,dev_tools_hot_reload
app = Dash(__name__, suppress_callback_exceptions= suppress_callback_exceptions)
app.title = titre
# Layout principal
app.layout = html.Div([
    dcc.Location(id="url"),
    navbar.navbar(),
    html.Div(id="page-content"),
    footer()
])
# Register callbacks
register_callbacks(app)
# Register callbacks2
register_callbacks2(app)
register_callbacks3(app)
register_callbacks4(app)
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
    elif pathname == "/regions":
        return regions_page()
    elif pathname == "/description":
        return description_page()
    else:
        return home_page()
    
if __name__ == "__main__":
    if not os.path.exists("data/raw/data_already_downloaded.flag"):  # Vérifie si un fichier indicateur existe
        startDownload()
        starCleaning()
        cleanDataByDept()
        with open("data/raw/data_already_downloaded.flag", "w") as f:  # Crée un fichier indicateur après le téléchargement
            f.write("Download completed.")
    app.run_server( host=host, port=port, debug=debug,use_reloader=use_reloader,use_debugger=use_debugger,dev_tools_ui=dev_tools_ui,dev_tools_hot_reload=dev_tools_hot_reload)
