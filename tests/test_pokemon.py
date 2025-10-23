import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADERS = {'Content-Type': 'application/json',
           'trainer_token': TOKEN}    # Вставить свой токен
TRAINER_ID = 'TRAINER_ID' #Вставить свой trainer_id


def test_trainers():
    respons_trainers = requests.get(
        url=f'{URL}/trainers', params={'level': '5'})
    assert respons_trainers.status_code == 200



def test_my_trainer():
    response_parametrize = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()['data'][0]['id'] == TRAINER_ID
