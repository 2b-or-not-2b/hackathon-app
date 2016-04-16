import json

from django.http import JsonResponse
from django.shortcuts import render
from mongoengine import DoesNotExist

from cashtag.models import CashTag
from users.models import CashTagUser

__author__ = '2b||!2b'


# ### FURTHER ROUTING FUNCTIONS ### #
def profile_view(request):
    return JsonResponse({}, status=401)


def feed_view(request):
    return JsonResponse({}, status=401)


def payment_view(request):
    return JsonResponse({}, status=401)


def cashtag_view(request):
    print('Saw request for cashtag')
    if request.method == 'POST':
        return cashtag_create(request)
    if request.method == 'GET':
        # if request.GET.get('logged_in'):
        #     return cashtag_view_get_not_logged_in(request)
        # return cashtag_view_get_not_logged_in(request)
        return cashtag_view_get(request)
    return JsonResponse({}, status=401)


# #### UTIL FUNCTIONS FOR ACTUAL CODE #### #


def cashtag_view_get(request):
    pk = request.GET['pk']
    try:
        cashtag = CashTag.objects.get(pk=pk)
        return JsonResponse(cashtag.to_api_json(), status=200)
    except DoesNotExist:
        return JsonResponse({'err': 'Not Foubnd'}, status=404)


def cashtag_view_get_not_logged_in(request):
    raise NotImplementedError


def cashtag_view_post_not_logged_in(request):
    raise NotImplementedError


def timeline_view_get(request):
    raise NotImplementedError


def cashtag_create(request):
    print('creating cashtag')
    post_data = json.loads(request.body.decode('utf-8'))

    creator_username = post_data.get('creator_username')
    title = post_data.get('title')
    min_price = post_data.get('min_price')
    tag_type = post_data.get('tag_type')
    description_txt = post_data.get('description_txt')
    description_html = post_data.get('description_html')
    video = post_data.get('video')
    image = post_data.get('image')
    rewards = post_data.get('rewards')

    video = video or None
    image = image or None
    rewards = rewards or None
    print('finished fetching data from POST')

    cashtag = CashTag(
        creator_username=creator_username,
        title=title,
        min_price=min_price,
        tag_type=tag_type,
        description_txt=description_txt,
        description_html=description_html,
        video=video,
        image=image,
        rewards=rewards,
    )
    if cashtag.validate_cashtag():
        print('validated!')
        try:
            cashtag.save()
            print('saved succesfully!')
            try:
                create_user = CashTagUser.objects.get(username=creator_username)
                create_user.cashtags_created_active.append(str(cashtag.pk))
                create_user.save()
            except DoesNotExist:
                # hackathon, that's fine
                print('user {} not found. Continuing anyways (because hackathon)'.format(creator_username))
                pass
        except Exception as e:
            print(e)
            exit()

    try:
        return JsonResponse(cashtag.to_api_json(), status=201)
    except Exception as e:
        print(e)
        exit()
