import requests

def creat_city(city):
    city += (', France' * 8)
    return city

base_url = "https://nominatim.openstreetmap.org/search"

params = {
    "q": creat_city("Treignac"),
    "format": "json"
}

def get_osm_data(params):
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la requête:", response.status_code)
        return None

paris_data = get_osm_data(params)

if paris_data:
    print(paris_data)
else:
    print("Aucune donnée n'a été récupérée.")
