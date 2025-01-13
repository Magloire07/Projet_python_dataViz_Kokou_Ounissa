import pandas as pd 
import json
from statistics import mean 
from pathlib import Path


def starCleaning():

    data= pd.read_csv("data/raw/labouref-france-departement-quarter-jobseeker.csv",sep=";")
    presi_data= pd.read_csv("data/raw/presiData.csv",sep=",")


    periodes= data["Période (Trimestre)"].apply(lambda x: x[:4])
    categories = data["Catégorie"]

    nom=presi_data["nom_president"]
    mandat=presi_data["mandat"]

    listUniquePeriode=     sorted(set(periodes))
    listUniqueCategories=  sorted(set(categories))

    #crée un repertoire pour chaque president 
    def createDir():
        for n in nom:
            Path(f"data/cleaned/{n}").mkdir(exist_ok=True)

    def cleanData(listPeriode,nomPresi):
        listSommeNbDemEmp=[]
        for cat in listUniqueCategories:
            print(cat)
            data_by_cat= data[ data["Catégorie"] == cat ] # on extraite  les  observations par catégories
            for  p in listPeriode:
                # on extrait et somme les nombre de demandeur  d'emploie par periode
                listSommeNbDemEmp.append( mean((data_by_cat[ (data_by_cat["Période (Trimestre)"].apply(lambda x: x[:4])==str(p))])["Nb moyen demandeur emploi"]))
            dico_by_cat= {"periodes":listPeriode, "nombre_demandeur_emploi":listSommeNbDemEmp}
            # on écrit au format json les données à afficher en fonction des catégories 
            with open(f"data/cleaned/{nomPresi}/listSommecat_{cat}.json","w") as file:
                json.dump(dico_by_cat, file, indent=4, ensure_ascii=False)
            listSommeNbDemEmp=[] # on vide pour la prochaine catégorie

    createDir()
    for n, m in zip(nom,mandat):
        min_=int(min(listUniquePeriode))
        if m!= "Mandat en cours":
            debut=m[:4]
            fin  =m[7:]
            l= [ annee for annee in range(int(debut), int(fin)+1)]
            if min_ in l:
                l= [ x for x in range(min_, max(l)+1)]
            if min(l)>= min_:
                cleanData(l,n)
        else:
            debut= (mandat.iloc[1])[7:]
            l=[ annee for annee in range(int(debut), 2024)]
            cleanData(l,n)

