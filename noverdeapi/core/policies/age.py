
import datetime


def analyze(data):
    birthdate = datetime.datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return ('aprovado', None) if age >= 18 else ('negado', None)
