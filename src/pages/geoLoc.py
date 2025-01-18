
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




# import pandas as pd
# import plotly.express as px
# from dash import dcc, html , Dash

# def map_page():

#         # Charger les données des communes
#         communes_df = pd.read_json("data/cleaned/communes_reduit.json")
#         print('1')
#         # Charger les données du chômage
#         chomage_df = pd.read_csv("data/raw/labouref-france-departement-quarter-jobseeker.csv", sep=";")
#         print('2')

#         # Convertir les colonnes 'dep_code' et 'Code Officiel Département' en string pour éviter les erreurs de fusion
#         communes_df['dep_code'] = communes_df['dep_code'].astype(str)
#         print('3')

#         chomage_df['Code Officiel Département'] = chomage_df['Code Officiel Département'].astype(str)
#         print('4')

#         # Fusionner les deux DataFrames sur les codes de départements
#         merged_df = pd.merge(communes_df, chomage_df, left_on='dep_code', right_on='Code Officiel Département', how='left')
#         print('')

#         # Calculer le taux de chômage en pourcentage de la population
#         merged_df['taux_chomage'] = (merged_df['Nb moyen demandeur emploi'] / merged_df['population']) * 100
        
#         # Préparer les données pour la carte
#         fig = px.scatter_mapbox(
#             merged_df,
#             lat="latitude_centre",
#             lon="longitude_centre",
#             color="taux_chomage",
#             hover_name="dep_nom",
#             hover_data=["taux_chomage", "population"],
#             zoom=5,
#             title="Carte de géolocalisation et taux de chômage par commune",
#             height=850
#         )
        
#         # Choisir le style de carte
#         fig.update_layout(mapbox_style="open-street-map")
        
#         # Créer la page avec le graphique
#         return html.Div([
#             html.H1("Localisation spatiale et taux de chômage", style={"text-align": "center"}),
#             dcc.Graph(figure=fig)
#         ])
