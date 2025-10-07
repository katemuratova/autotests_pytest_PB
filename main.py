import requests

URL = 'https://api.pokemonbattle.ru/v2'
HEADERS = {'Content-Type':'application/json', 'trainer_token' : '006bec7e9901754d36a7482a66d2e7bd'}

body_create_pokemon = {
    "name": "Тирмазавр",
    "photo_id": 298
}

body_rename_pokemon = {
    "pokemon_id": "405321",
    "name": "Бублик",
    "photo_id": 576
}

body_add_pokeball = {
    "pokemon_id": "405323"
}

# create_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADERS, json=body_create_pokemon)
# print(create_pokemon.text)

# rename_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=body_rename_pokemon)
# print(rename_pokemon.text)

add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_add_pokeball)
print(add_pokeball.text)