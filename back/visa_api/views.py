from django.http import JsonResponse
from django.shortcuts import render

from visa_api.util import pull, push


def test_push_pull_view(request):
    pull_response = pull()
    push_response = push()
    return JsonResponse({
        'pull_response': str(pull_response),
        'push_response': str(push_response),
    })
