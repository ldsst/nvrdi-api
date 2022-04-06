
import requests
from django.conf import settings


def query_score(cpf):
    url = 'https://challenge.noverde.name/score'
    headers = {'x-api-key': settings.X_API_KEY}
    payload = {'cpf': cpf}

    response = requests.post(url, json=payload, headers=headers)

    score = response.json()['score']
    return score


def query_commitment(cpf):
    url = 'https://challenge.noverde.name/commitment'
    headers = {'x-api-key': settings.X_API_KEY}
    payload = {'cpf': cpf}

    response = requests.post(url, json=payload, headers=headers)

    commitment = response.json()['commitment']
    return commitment
