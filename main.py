import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN' # Указать токен тренера
HEADERS = {'Content-Type':'application/json', 'trainer_token' : TOKEN} # Указать токен тренера
body_registration= {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}

body_create_pokemon = {
    "name": "POKEMON_NAME",
    "photo_id": 298
}

body_rename_pokemon = {
    "pokemon_id": "POKEMON_ID", # Указать pokemon_id своего покемона
    "name": "NEW NAME",
    "photo_id": 576
}

body_add_pokeball = {
    "pokemon_id": "POKEMON_ID" # Указать pokemon_id своего покемона
}

# Можно использовать любой запрос:

# registration = requests.post(url = f'{URL}/trainers/reg',headers = HEADERS,json = body_registration)
# print(registration.text)

# response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email',headers = HEADERS,json = body_confirmation)
# print(response_confirmation.text)

# create_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADERS, json=body_create_pokemon) 
# print(create_pokemon.text)

# rename_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADERS, json=body_rename_pokemon)
# print(rename_pokemon.text)
 
# add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADERS, json=body_add_pokeball)
# print(add_pokeball.text)
