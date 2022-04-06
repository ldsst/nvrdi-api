
from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreditRequest(Base):

    # Campos criados durante a criação da solicitação.
    uuid = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name='Nome')
    cpf = models.CharField(max_length=200, verbose_name='CPF')
    birthdate = models.DateField(verbose_name='Data de nascimento')
    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor desejado')
    terms = models.IntegerField(verbose_name='Quantidade de parcelas desejadas')
    income = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Renda mensal')

    # Campos resultado da aprovação.
    status = models.CharField(max_length=200, default='processing')  # processing, completed
    result = models.CharField(max_length=200, null=True, blank=True)  # approved, refused
    refused_policy = models.CharField(max_length=200, null=True, blank=True)  # age, score,commitment
    approved_amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Montante aprovado', blank=True,
                                          null=True)
    approved_terms = models.IntegerField(verbose_name='Quantidade de parcelas aprovadas', blank=True, null=True)
