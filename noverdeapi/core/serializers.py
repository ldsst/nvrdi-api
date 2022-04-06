
from rest_framework import serializers
from django.conf import settings


class RequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    cpf = serializers.CharField(max_length=200)
    birthdate = serializers.DateField(format='%Y-%m-%d')
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=1000, max_value=4000)
    terms = serializers.IntegerField()
    income = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_terms(self, value):
        if value not in settings.TERMS:
            raise serializers.ValidationError(f"O valor deve ser igual a {', '.join([str(x) for x in settings.TERMS])}")
        return value


class CreditRequestSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200, source='uuid')
    status = serializers.CharField(max_length=200)
    result = serializers.CharField(max_length=200)
    refused_policy = serializers.CharField(max_length=200)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False, source='approved_amount')
    terms = serializers.IntegerField(source='approved_terms')
