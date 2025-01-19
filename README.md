<b>Kokou et Ounissa </b> <br>

# Infos sur de projet Mdpol&Emploi
<b> Bienvenue sur la page de notre projet concernant une étude des taux de chômages et du nombre de demandeurs d'emploi en France en fonction du temps et des régions allignée sur les mandats présidentiels allant de Jacques Chirac à Emmanuel Marcon. </b> <br>
![MDPOL&EMPLOI](/assets/dashboard.png)


## User Guide

### installation des dépenddances 
`$ python -m pip install -r requirements.txt`
###  Premier lancement du projet
Si le repertoires  `data/cleaned` est vide alors assurez-vous de suprimer s'il existe, le fichier `data_already_downloaded.flag` avant le lancer le projet
### lancement du projet (`python>=3.0`)
`$ python main.py`


##  Data

`------fichier .csv -----`

- ### csv emploi 1996- 2023
    - [cliquez ici](https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/labouref-france-departement-quarter-jobseeker/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B)
- ### csv  geolocalisation
    - [cliquez ici](https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B)
- ### csv emploi 2007-2012
    - [cliquez ici](https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/base-cc-caract-emploi-2012-arm/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B)
- ### csv  population
    - [cliquez ici](https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/demographyref-france-pop-legale-commune-arrondissement-municipal-millesime/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B)


`----- site  source ------`

### dataset geolocalisation départements 
[cliquez ici](https://public.opendatasoft.com/explore/dataset/correspondance-code-insee-code-postal/table/?location=3,18.5278,-2.98684&basemap=jawg.light)
    

### dataset emploi 2007-2012
[cliquez ici](https://public.opendatasoft.com/explore/dataset/base-cc-caract-emploi-2012-arm/information/?sort=actifs_occupes_15_ans_ou_plus_en_2007_princ&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6ImJhc2UtY2MtY2FyYWN0LWVtcGxvaS0yMDEyLWFybSIsIm9wdGlvbnMiOnsic29ydCI6ImFjdGlmc19vY2N1cGVzXzE1X2Fuc19vdV9wbHVzX2VuXzIwMDdfcHJpbmMifX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJBVkciLCJ5QXhpcyI6ImNvZGVfZ2VvZ3JhcGhpcXVlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ZGNTE1QSJ9XSwieEF4aXMiOiJhbm5lZSIsIm1heHBvaW50cyI6NTAsInNvcnQiOiIifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=3,18.54017,-3.01253&basemap=jawg.light)

### dataset emploi 1996- 2023
[cliquez ici](https://public.opendatasoft.com/explore/dataset/labouref-france-departement-quarter-jobseeker/export/?disjunctive.category&disjunctive.age_groups&disjunctive.reg_name&disjunctive.dep_area_code&disjunctive.dep_name&sort=date&refine.category=B&refine.category=C&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW5yYW5nZSIsImZ1bmMiOiJDT1VOVCIsInlBeGlzIjoibmJfam9ic2Vla2VyIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoicmFuZ2UtY3VzdG9tIiwiY2hhcnRzIjpbeyJmdW5jIjoiTUlOIiwieUF4aXMiOiJuYl9qb2JzZWVrZXIifSx7ImZ1bmMiOiJNQVgiLCJ5QXhpcyI6Im5iX2pvYnNlZWtlciJ9XX1dLCJ4QXhpcyI6ImRhdGUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOiJ5ZWFyIiwic29ydCI6IiIsInNlcmllc0JyZWFrZG93biI6ImNhdGVnb3J5IiwiY29uZmlnIjp7ImRhdGFzZXQiOiJsYWJvdXJlZi1mcmFuY2UtZGVwYXJ0ZW1lbnQtcXVhcnRlci1qb2JzZWVrZXIiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmNhdGVnb3J5Ijp0cnVlLCJkaXNqdW5jdGl2ZS5hZ2VfZ3JvdXBzIjp0cnVlLCJkaXNqdW5jdGl2ZS5yZWdfbmFtZSI6dHJ1ZSwiZGlzanVuY3RpdmUuZGVwX2FyZWFfY29kZSI6dHJ1ZSwiZGlzanVuY3RpdmUuZGVwX25hbWUiOnRydWUsInNvcnQiOiJkYXRlIiwicmVmaW5lLmNhdGVnb3J5IjpbIkIiLCJDIl19fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlLCJ0aW1lc2NhbGUiOiIifQ%3D%3D)  


### dataset relatives aux populations légales 2018- 2023
[cliquez ici](https://public.opendatasoft.com/explore/dataset/demographyref-france-pop-legale-commune-arrondissement-municipal-millesime/information/?disjunctive.reg_code&disjunctive.reg_name&disjunctive.dep_code&disjunctive.arrdep_code&disjunctive.com_arm_code&disjunctive.com_arm_name&disjunctive.epci_name&disjunctive.epci_code&disjunctive.dep_name&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6ImRlbW9ncmFwaHlyZWYtZnJhbmNlLXBvcC1sZWdhbGUtY29tbXVuZS1hcnJvbmRpc3NlbWVudC1tdW5pY2lwYWwtbWlsbGVzaW1lIiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5yZWdfY29kZSI6dHJ1ZSwiZGlzanVuY3RpdmUucmVnX25hbWUiOnRydWUsImRpc2p1bmN0aXZlLmRlcF9jb2RlIjp0cnVlLCJkaXNqdW5jdGl2ZS5hcnJkZXBfY29kZSI6dHJ1ZSwiZGlzanVuY3RpdmUuY29tX2FybV9jb2RlIjp0cnVlLCJkaXNqdW5jdGl2ZS5jb21fYXJtX25hbWUiOnRydWUsImRpc2p1bmN0aXZlLmVwY2lfbmFtZSI6dHJ1ZSwiZGlzanVuY3RpdmUuZXBjaV9jb2RlIjp0cnVlLCJkaXNqdW5jdGl2ZS5kZXBfbmFtZSI6dHJ1ZX19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJwaWUiLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6ImNvbV9hcm1fcG9wX211biIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6InJhbmdlLWN1c3RvbSIsInBvc2l0aW9uIjoiY2VudGVyIn1dLCJ4QXhpcyI6Imdlb195ZWFyIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoieWVhciIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiIiLCJzZXJpZXNCcmVha2Rvd25UaW1lc2NhbGUiOiIifV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9)  




## Rapport d'analyse
### Analyse selon les mandats présidentiels :
`Emmanuel Macron`
En cinq ans le chômage est passé de 9,5% de la population active à 7,4%, avec un mandat toujours en cours.

`Nicolas Sarkozy`
Confronté à la crise des subprimes, le mandat de Nicolas Sarkozy a vu le chômage passer de 8,1 à 9,5% de la population active.

`François Hollande`
Le mandat François Hollande n'aura pas donné lieu à une baisse spectaculaire du taux de chômage.

`Jacques Chirac`
La France connaît au début du quinquennat Chirac un taux de chômage supérieur à 10%. La baisse entamée en 1998 se poursuit durant la cohabitation et passe sous la barre des 8% en 2001.

###  Analyse selon les diagrammes en anneaux :
On observe d'après le diagramme en anneaux que la taux de chomeurs n'est pas proportionnel à la densité de la population 
Il y a donc une disparité disproportionnelle dans la repartion des offres d'emploi.

###  Analyse selon les régions :

D'après les différentes courbes des évolutions dans les différents départements de France, on observe que :
* L'évolution du taux de chômage dans les régions suit les tendances nationales
* Quasi toutes les courbes suivent le même cheminement : 
* *  Un <b>pic lors de l'arrivée au pouvoir de Jacques Chirac </b>, 
* *  Une <b>baisse significative </b> du nombre de demandeurs d'emploi durant son premier mandat,
* *  Un <b> leger regain </b>au milieu de son second mandat, 
* *  Une <b> stabilisation au plus bas niveau </b> entre la fin du mandat de Chirac et le début de celui de Sarkozy,
* *  Une <b> augmentation stable </b> depuis, atteignant <b> un pic en 2015 sous Hollande, ou en 2020 sous Macron </b> .  <br>

Pour résumer, la France connait une tendance globale à la hausse du chômage. Cette hausse est surtout très sensible aux crises économiques modiales (2008, Covid-19).

## Developer Guide
- l'ajout d'un graphe se fait dans le fichier `src/pages/graph.py` en rajoutant à la methode `graph_page()` le composant du graphe 
- Pour ajouter une page il faut rajouter le fichier .py   au  repertoire `src/pages` puis l'importer dans le `main.py` sans oublier de rajouter le chemin de routage à la structure conditionnelle écrite à cet effet. Le fichier `src/components/navbar.py permet d'ajouter la page dans une liste non ordonnée.

## main.py
```mermaid
graph TD
    App_Layout --> url[url]
    App_Layout --> navbar[navbar]
    App_Layout --> page-content[page-content]
    App_Layout --> footer[footer]
    url[url] -->|Callback| page-content[page-content]
```
## regions.py

```mermaid
graph TD
    A[cleanDataByDept] -->|Reads CSV| B[Chômage Data]
    A --> C[Extracts Year and Quarter]
    C --> D[Write Departments to File]
    A --> E[Generate Department JSON Files]
    E --> F[Data Aggregation by Department]
    F --> G[Write JSON for Each Department]
    E --> H[Create Taux Chômage JSON]
    
    B -->|Departments List| I[Departements Array]
    I --> D
    
    subgraph Mandats
        M1[Jacques Chirac] --> M2[Nicolas Sarkozy]
        M2 --> M3[François Hollande]
        M3 --> M4[Emmanuel Macron]
    end
    
    G -->|Department Data by Mandat| J[Graph Generation with Plotly]
    J --> K[Dynamic Graph Callback]
    K --> L[Update Graph with Data]
    K --> M[Graph Type Selector]
    M --> L
    M --> N[Dynamic Department Selector]
    N --> L
    
    subgraph Output
        L --> O[Display Graph]
        O --> P[Visualize Mandat Colors]
    end

    classDef Mandats fill:#f9f,stroke:#333,stroke-width:4px;
    class M1,M2,M3,M4 Mandats;

```

## home.py

```mermaid
graph TD
    A[home_page] --> B[Main Container]
    B --> C[Bienvenue Div]
    C --> D[H1: Bienvenue sur MDPOL & EMPLOI!]
    B --> E[Description Paragraph]
    E --> F[P: Impact sur le marché de l'emploi des politiques économiques]
    B --> G[Background Image]
    G --> H[Img: Ministere_travail.jpeg]
    
    classDef main fill:#f9f,stroke:#333,stroke-width:4px;
    class B main;
    
    classDef description fill:#ccf,stroke:#333,stroke-width:2px;
    class E description;
```
## graph.py

```mermaid
flowchart TD
    A[Graph Page Layout] --> B[Options Section]
    A --> C[Graphs Section]
    C --> D[Graph 1: Dynamic Graph]
    C --> E[Graph 2: Dynamic Graph]
    C --> F[Graph 3: Dynamic Graph]
    C --> G[Graph 4: Dynamic Graph]
    C --> H[Donut Charts]
    H --> I[Donut 1: Unemployment Rate]
    H --> J[Donut 2: Population Density]

    B --> K[Dropdown for Chart Type]
    B --> L[Radio Buttons for Categories]

    D --> M[Callback: Dynamic Graph Update]
    E --> M
    F --> M
    G --> M

    I --> N[Callback: Update Donut 1]
    J --> O[Callback: Update Donut 2]

    M --> P[Data Fetch: JSON Files]
    N --> P
    O --> P
    P --> Q[Data Processing: Calculations]
    Q --> R[Graph Update: Plotly Express]

    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#ffcc00,stroke:#333,stroke-width:2px
    style C fill:#ffcc00,stroke:#333,stroke-width:2px
    style D fill:#99ff99,stroke:#333,stroke-width:2px
    style E fill:#99ff99,stroke:#333,stroke-width:2px
    style F fill:#99ff99,stroke:#333,stroke-width:2px
    style G fill:#99ff99,stroke:#333,stroke-width:2px
    style H fill:#ffcc00,stroke:#333,stroke-width:2px
    style I fill:#66ccff,stroke:#333,stroke-width:2px
    style J fill:#66ccff,stroke:#333,stroke-width:2px
    style K fill:#e6f7ff,stroke:#333,stroke-width:2px
    style L fill:#e6f7ff,stroke:#333,stroke-width:2px
    style M fill:#f2f2f2,stroke:#333,stroke-width:2px
    style N fill:#f2f2f2,stroke:#333,stroke-width:2px
    style O fill:#f2f2f2,stroke:#333,stroke-width:2px
    style P fill:#f2f2f2,stroke:#333,stroke-width:2px
    style Q fill:#ffcc99,stroke:#333,stroke-width:2px
    style R fill:#ffcc99,stroke:#333,stroke-width:2px

```
## geoLoc.py
```mermaid
flowchart TD
    A[Map Page] --> B[Create DataFrame]
    B --> C[Create Scatter Mapbox]
    C --> D[Update Map Style]
    D --> E[Return HTML Layout]
    
    A --> F[Title: Localisation spatiale]
    A --> G[Graph: Geolocalization Map]

    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#ffcc00,stroke:#333,stroke-width:2px
    style C fill:#99ff99,stroke:#333,stroke-width:2px
    style D fill:#ffcc99,stroke:#333,stroke-width:2px
    style E fill:#ffcc00,stroke:#333,stroke-width:2px
    style F fill:#e6f7ff,stroke:#333,stroke-width:2px
    style G fill:#e6f7ff,stroke:#333,stroke-width:2px
```
## description.py
```mermaid
flowchart TD
    A[Description Page] --> B[Read Text File]
    B --> C[Store Lines in List]
    C --> D[Create HTML Layout]
    
    D --> E[Title: DESCRIPTION DES CATÉGORIES]
    D --> F[Paragraph: File Lines]

    style A fill:#f9f,stroke:#333,stroke-width:4px
    style B fill:#ffcc00,stroke:#333,stroke-width:2px
    style C fill:#99ff99,stroke:#333,stroke-width:2px
    style D fill:#ffcc99,stroke:#333,stroke-width:2px
    style E fill:#e6f7ff,stroke:#333,stroke-width:2px
    style F fill:#e6f7ff,stroke:#333,stroke-width:2px
```
## get_data.py
```mermaid
graph TD
    A[Start] --> B[Download CSV Files]
    B --> C[Fetch Data from URLs]
    C --> D[Download File from URL]
    D --> E[Save File to Directory]
    E --> F[Presidency Data Fetch]
    F --> G[Scrape French Presidents Data]
    G --> H[Parse HTML with PresidencyParser]
    H --> I[Handle Errors if any]
    I --> J[End]

    classDef startEnd fill:#f9f,stroke:#333,stroke-width:4px;
    class A,J startEnd;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    class B,C,D,E,F,G,H process;
    classDef error fill:#fbb,stroke:#333,stroke-width:2px;
    class I error;
```
## presidenceParser.py
```mermaid
graph TD
    A[Start] --> B[Initialize Parser]
    B --> C[Create Output File]
    C --> D[Parse HTML Start Tag]
    D --> E[Check if inside galery]
    E --> F[Inside Link a Tag?]
    F --> G[Capture Data Inside a Tag]
    G --> H[Write Data to CSV]
    H --> I[Parse HTML End Tag]
    I --> J[Is Link Tag Closed?]
    J --> K[Reset Current Text]
    K --> L[Check for ul End Tag]
    L --> M[End Parsing]

    classDef startEnd fill:#f9f,stroke:#333,stroke-width:4px;
    class A,M startEnd;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    class B,C,D,E,F,G,H,I,J,K,L process;
```
## communes.py
```mermaid
graph TD
    A[Start] --> B[Load JSON File]
    B --> C[Check for data Key]
    C --> D{Is data Key Present?}
    D -->|No| E[Raise KeyError]
    D -->|Yes| F[Filter Data Columns]
    F --> G[Create New Data Structure]
    G --> H[Save Filtered Data to File]
    H --> I[End]

    classDef startEnd fill:#f9f,stroke:#333,stroke-width:4px;
    class A,I startEnd;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    class B,C,D,F,G,H process;
```
## clean_data.py
```mermaid
graph TD
    A[Start] --> B[Load Data Jobseeker, Presidency, Population]
    B --> C[Extract Unique Periods & Categories]
    C --> D[Create Directory for Each President]
    D --> E[Loop Through Presidents and Mandates]
    E --> F{Is the Mandate In Progress?}
    F -->|No| G[Clean Data for Historical Periods]
    F -->|Yes| H[Clean Data for Current Period]
    G --> I[Save Data by Category JSON]
    H --> I[Save Data by Category JSON]
    I --> J[Clean Population Data]
    J --> K[Save Population Data JSON]
    K --> L[End]

    classDef startEnd fill:#f9f,stroke:#333,stroke-width:4px;
    class A,L startEnd;
    classDef process fill:#bbf,stroke:#333,stroke-width:2px;
    class B,C,D,E,F,G,H,I,J,K process;

```
## Copyright &copy; 
 Nous déclarons sur l’honneur que le code fourni a été produit par nous, masters et contributeurs du depôt git ci-contre 
https://github.com/Magloire07/Projet_python_dataViz_Kokou_Ounissa.git
.



