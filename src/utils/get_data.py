import os
import requests
import urllib.request
from src.utils.PresidencyParser import PresidencyParser

def download_file_auto(url, save_directory):
    os.makedirs(save_directory, exist_ok=True) # Crée le répertoire si nécessaire
    
    # on recupère le nom du fichier depuis l'en-tête HTTP "Content-Disposition"
    response = requests.head(url)
    if "Content-Disposition" in response.headers:
        filename = response.headers["Content-Disposition"].split("filename=")[-1].strip('"')

    save_path = os.path.join(save_directory, filename)  # Chemin complet pour enregistrer le fichier
    
    try:
        # Téléchargement du fichier
        response = requests.get(url, stream=True)        
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):  # Télécharge par blocs de 8 Ko
                file.write(chunk)
        print(f"Fichier téléchargé avec succès : {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement : {e}")

UrlList=list()
save_directory = "data/raw/"
# on ajoute des fichiers.csv à télécharger
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/labouref-france-departement-quarter-jobseeker/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/base-cc-caract-emploi-2012-arm/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/demographyref-france-pop-legale-commune-arrondissement-municipal-millesime/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
def  startDownload():
    for url in UrlList:
        download_file_auto(url, save_directory)
    #
    #recupération de la liste des présidents 
    url = "https://www.elysee.fr/la-presidence/les-presidents-de-la-republique"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        html_data = response.read().decode('utf-8')
        parser = PresidencyParser()
        parser.feed(html_data)
    except urllib.error.URLError as e:
        print(f"Erreur lors de l'accès à l'URL : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")










