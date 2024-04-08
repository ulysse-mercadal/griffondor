import requests

def creat_city(city):
    city += (', France' * 8)
    return city

# Définition de l'URL de base de l'API OpenStreetMap
base_url = "https://nominatim.openstreetmap.org/search"

# Paramètres de la requête
params = {
    "q": creat_city("Treignac"),  # Query : le lieu ou l'adresse que vous recherchez
    "format": "json"        # Format de sortie des données (json, xml, etc.)
}

# Fonction pour effectuer la requête à l'API OpenStreetMap
def get_osm_data(params):
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la requête:", response.status_code)
        return None

# Exemple d'utilisation de la fonction pour récupérer les données géographiques de Paris
paris_data = get_osm_data(params)

# Affichage des données récupérées
if paris_data:
    print(paris_data)
else:
    print("Aucune donnée n'a été récupérée.")
