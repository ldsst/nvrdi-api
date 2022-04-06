
from ..api import query_score


def analyze(data):
    score = query_score(data['cpf'])
    return ('aprovado', None) if score >= 600 else ('negado', None)
