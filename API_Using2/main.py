import requests

base_url = "https://rickandmortyapi.com/api/"

def get_character(character_):
    response = requests.get(f"{base_url}character/?name={character_name}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get character {character_name}, status code: {response.status_code}")
        return None

#character_name = input("Enter the character's name: ")
character_name = ("Jerry Smith")
character_data = get_character(character_name)

if character_data:
    print("Character name:", character_data['results'][0]['name'])
    print("Character status:", character_data['results'][0]['status'])
    print("Character species:", character_data['results'][0]['species'])
    print("Character type:", character_data['results'][0]['type'])
    print("Character gender:", character_data['results'][0]['gender'])