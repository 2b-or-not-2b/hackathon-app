from django.http import JsonResponse
from django.shortcuts import render

from users.models import CashTagUser


def user_view(request):
    if request.method == 'POST':
        raise NotImplementedError
    if request.method != 'GET':
        return JsonResponse({}, status=401)

    username = request.GET['username']
    user = CashTagUser.objects.get(username=username)

    return JsonResponse(user.to_api_json())


