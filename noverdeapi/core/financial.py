
import os
import numpy as np
from yaml import safe_load
from .api import query_score
from django.conf import settings


def calculate_pmt(cpf, pv, n):
    score = query_score(cpf)
    rate = select_rate(score, n)/100
    pmt = np.pmt(rate, n, pv)
    return abs(round(pmt, 2))


def select_rate(score, n):
    rates_path = os.path.join(settings.BASE_DIR, 'core', 'etc', 'rates.yml')
    with open(rates_path, 'r') as stream:
        rates_per_range = safe_load(stream)
        selected_range = __get_range(rates_per_range, score)
        rate = __get_rate(selected_range, n)
        return rate


def __get_range(rates, score):
    for key, value in rates['rates_per_range'].items():
        minimum, maximum = (int(n) for n in key.split('-'))
        if minimum <= score <= maximum:
            return value


def __get_rate(rates_per_range, n):
    for key, value in rates_per_range.items():
        if key == n:
            return value
