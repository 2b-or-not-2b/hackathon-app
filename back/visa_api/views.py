from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render

from cashtag.models import CashTag
from users.models import CashTagUser
from visa_api.util import pull, push


def test_push_pull_view(request):
    # from_username = request.GET.get('from_username')
    cashtag_id = request.GET.get('cashtag_id')
    amount = request.GET.get('amount')
    amount = Decimal(amount)
    assert amount > 0
    assert amount < 9999

    pull_response = pull()
    push_response = push()

    # user = CashTagUser.objects.get(username=from_username)
    cash_tag = CashTag.objects.get(int_id=cashtag_id)
    cash_tag.money_collected += amount
    cash_tag.supporters.append('neil')  # laziness, whatever
    cash_tag.save()

    return JsonResponse({
        'pull_response': str(pull_response),
        'push_response': str(push_response),
        'raised_money': cash_tag.money_collected
    })

