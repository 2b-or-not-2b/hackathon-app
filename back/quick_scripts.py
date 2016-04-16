import requests
from mongoengine import DoesNotExist

from users.models import CashTagUser
from util.mongo_utils import connect_to_mongodb_if_not_connected

__author__ = '2b||!2b'


def post_cashtag():
    print('POSTing cashtag')
    data = {
        'creator_username': 'neil',
        'title': 'Fund Our Hackathon Team!',
        'min_price': '9999',
        'tag_type': 'support',
        'description_txt': 'We only get to hack for 24 hours, so give us money during that time or something!',
        'video': '',
        'image': '',
        'rewards': '',
    }

    response = requests.post(url='http://localhost:8000/api/cashtag', json=data)
    print(response)
    assert response.ok
    assert response.status_code == 201
    return response.json()['_id']


def get_posted_cashtag(pk):
    print('GETing {}'.format(pk))
    response = requests.get(url='http://localhost:8000/api/cashtag/?pk={}'.format(pk))
    print(response)
    assert response.ok
    assert response.status_code == 200
    assert response.json()['_id'] == pk


def create_test_users():
    print('Creating users')
    try:
        test_user = CashTagUser.objects.get(username='test_user')
    except DoesNotExist:
        test_user = CashTagUser(
            username='test_user',
            password='password',
        )
        test_user.save()

    user_info = ['neil', 'cody', 'daariel']
    users_created = []
    users_were_created_this_test = False
    for username in user_info:
        try:
            user = CashTagUser.objects.get(username=username)
        except DoesNotExist:
            users_were_created_this_test = True
            user = CashTagUser(
                username=username,
                password='password',
            )
            user.save()
        users_created.append(user)

    if users_were_created_this_test:
        for userA in users_created:
            for userB in users_created:
                if userA.pk == userB.pk:
                    continue
                userA.friends.append(str(userB.pk))
                userA.contacts.append(str(userB.pk))
            userA.contacts.append(str(test_user.pk))
            userA.save()
    print('users created')


def verify_test_users():
    user_info = ['neil', 'cody', 'daariel']
    for username in user_info:
        user = CashTagUser.objects.get(username=username)
        assert user.username == username
        try:
            assert len(user.friends) == 2
        except AssertionError:
            print('len(user.friends) ==')
            print(len(user.friends))
            exit()
        try:
            assert len(user.contacts) == 3
        except AssertionError:
            print('len(user.contacts) ==')
            print(len(user.contacts))
            exit()
    print('User creatiom verified')


if __name__ == '__main__':
    pk = post_cashtag()
    get_posted_cashtag(pk)

    connect_to_mongodb_if_not_connected()
    create_test_users()
    verify_test_users()

