import pandas as pd
import plotly.express as px
from dash import dcc, html

def map_page():
    # Exemple de données géographiques
    data = pd.DataFrame({
        "Ville": ["Paris", "Lyon", "Marseille"],
        "Latitude": [48.8566, 45.7640, 43.2965],
        "Longitude": [2.3522, 4.8357, 5.3698]
    })
    fig = px.scatter_mapbox(
        data,
        lat="Latitude",
        lon="Longitude",
        text="Ville",
        zoom=5,
        title="Carte de géolocalisation",
        height=850
        
    )
    fig.update_layout(mapbox_style="open-street-map")

    return html.Div([
        html.H1("Localisation spaciale ", style={"text-align": "center"}),
        dcc.Graph(figure=fig)
    ])
