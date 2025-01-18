import json

# Chemin vers le fichier JSON volumineux
input_file = "/data/raw/communes.json"
output_file = "/data/cleaned/communes_simple.json"

# Colonnes à conserver
columns_to_keep = [
    "dep_code", 
    "dep_nom", 
    "latitude_centre", 
    "longitude_centre", 
    "population"
]

# Charger le fichier JSON
with open(input_file, "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Erreur lors de la lecture du fichier JSON : {e}")

# Vérifier la structure des données
if "data" not in data:
    raise KeyError("Le fichier JSON ne contient pas de clé 'data'.")

# Filtrer les colonnes
filtered_data = {
    "metadata": data.get("metadata", {}),
    "data": [
        {key: row[key] for key in columns_to_keep if key in row}
        for row in data["data"]
    ]
}

# Sauvegarder le fichier filtré
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=4)

print(f"Fichier réduit enregistré dans {output_file}")
