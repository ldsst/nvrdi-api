
from rest_framework import viewsets
from .models import CreditRequest
from .serializers import CreditRequestSerializer, RequestSerializer
from rest_framework.response import Response
from .tasks import register


class CreditRequestViewSet(viewsets.ViewSet):

    def create(self, request):
        try:
            # Faz a validação dos dados de entrada.
            serializer = RequestSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # Registra a tarefa a ser executada e recebe o UUID gerado.
            uuid = str(register.delay(request.data))

            # Retorna o UUID.
            return Response(status=201, data={'id': uuid})
        except Exception as err:
            errors = [dict(field=k, errors=v) for k, v in err.detail.items()]
            return Response(status=400, data=dict(errors=errors))

    def retrieve(self, request, pk=None):

        queryset = CreditRequest.objects.filter(uuid=pk).first()
        if queryset:
            serializer = CreditRequestSerializer(queryset)
            return Response(serializer.data)

        return Response(status=404, data=dict(errors='Solicitação de crédito não localizada'))
