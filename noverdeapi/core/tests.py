
from django.test import TestCase
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import CreditRequest
from .serializers import CreditRequestSerializer


client = Client()


class CreditRequestTest(TestCase):

    def setUp(self):
        self.dna = CreditRequest.objects.create(
            uuid='291691f5-9f46-48a9-b5fe-a4c4a3a21702', name='Douglas Noel Adams', cpf='12345678934',
            birthdate='1952-03-11', amount=1.200, terms=6, income=3000
        )

    def test_get_valid_uuid(self):
        response = client.get(
            reverse('loan-retrieve', kwargs={'pk': self.dna.uuid}))
        credit_request = CreditRequest.objects.get(uuid=self.dna.uuid)
        serializer = CreditRequestSerializer(credit_request)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_uuid(self):
        response = client.get(
            reverse('loan-retrieve', kwargs={'pk': '42'}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
