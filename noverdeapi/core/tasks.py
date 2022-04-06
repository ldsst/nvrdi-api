
import logging
import importlib
from celery import shared_task
from .models import CreditRequest
from django.conf import settings

logger = logging.getLogger('django')


def get_module_function(module_name):
    module_path = f'core.policies.{module_name}'
    spam_spec = importlib.util.find_spec(module_path)
    if spam_spec:
        module = importlib.import_module(module_path)
        return getattr(module, 'analyze')
    return None


def save_request(uuid, data):
    credit_request = CreditRequest(
        uuid=uuid,
        name=data['name'],
        cpf=data['cpf'],
        birthdate=data['birthdate'],
        amount=data['amount'],
        terms=data['terms'],
        income=data['income']
    )
    credit_request.save()
    return credit_request


def update_request(credit_request, status, result, refused_policy=None, approved_amount=None, approved_terms=None):
    credit_request.status = status
    credit_request.result = result
    credit_request.refused_policy = refused_policy
    credit_request.approved_amount = approved_amount
    credit_request.approved_terms = approved_terms
    credit_request.save()


@shared_task(name='tasks.register', bind=True)
def register(self, data):

    task_id = self.request.id
    credit_request = save_request(task_id, data)

    # Validação da existência da lista de políticas ativas.
    if not hasattr(settings, 'ACTIVE_POLICIES') or not settings.ACTIVE_POLICIES:
        update_request(credit_request, status='completed', result='error')
        raise Exception('O parâmetro ACTIVE_POLICIES nos settings do Django não existe ou não é uma lista com itens')

    results = []

    for i, policy in enumerate(settings.ACTIVE_POLICIES):
        fn = get_module_function(policy)
        if fn:
            policy_result = fn(data)
            results.append(dict(
                policy=policy,
                result=policy_result
            ))
        else:
            logger.info(f'Não existe implementação da política "{policy}"')

    if len(results) > 0:
        result = 'approved' if all(result['result'][0] == 'aprovado' for result in results) else 'refused'
        approved_amount = data['amount'] if result == 'approved' else None
        refused_policy = next((result['policy'] for result in results if result['result'][0] == 'negado'), None)
        approved_terms = next((result['result'][1] for result in results if result['result'][1] is not None), None)

        # Atualiza as informações da solicitação no banco.
        update_request(credit_request, status='completed', result=result, refused_policy=refused_policy,
                       approved_amount=approved_amount, approved_terms=approved_terms)
    else:
        update_request(credit_request, status='completed', result='error')
        raise Exception('Nenhum resultado foi obtido pela análise de crédito')
