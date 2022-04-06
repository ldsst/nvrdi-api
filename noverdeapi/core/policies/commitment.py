
from ..api import query_commitment
from ..financial import calculate_pmt
from django.conf import settings


def analyze(data):
    cpf = data['cpf']
    income = float(data['income'])
    terms = data['terms']
    amount = float(data['amount'])

    commitment = query_commitment(cpf)
    committed = commitment * income
    free = income - committed

    while terms != -1:
        pmt = calculate_pmt(cpf, amount, terms)
        if pmt < free:
            return 'aprovado', terms
        terms = next((term for term in settings.TERMS if term > terms), -1)

    return 'negado', None
