import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(pokemon_name):
    url = f"{base_url}/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Failed to get pokemon {pokemon_name}:{response.status_code}")
        return None

while True:
    pokemon_name = input("Enter the pokemon name: ")
    pokemon_data = get_pokemon(pokemon_name)

    if pokemon_data:
        print(f"Pokemon name: {pokemon_data['name'].capitalize()}")
        print(f"Pokemon id: {pokemon_data['id']}")
        print(f"Pokemon height: {pokemon_data['height']}")
        print(f"Pokemon weight: {pokemon_data['weight']}")
        print(f"Pokemon types: {pokemon_data['types']}")