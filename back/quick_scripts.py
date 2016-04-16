import requests
from mongoengine import DoesNotExist

from cashtag.models import CashTag
from users.models import CashTagUser
from util.mongo_utils import connect_to_mongodb_if_not_connected

__author__ = '2b||!2b'


def drop_dat_db():
    for cash_tag in CashTag.objects():
        cash_tag.delete()
    for cash_tag_user in CashTagUser.objects():
        cash_tag_user.delete()


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
    json_data = response.json()
    assert json_data['_id'] == pk
    assert json_data['creator_username'] == 'neil'

    neil_user = CashTagUser.objects.get(username='neil')
    print(neil_user.cashtags_created_active)
    assert pk in neil_user.cashtags_created_active


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

    user_info = ['neil', 'cody', 'dariel']
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
    user_info = ['neil', 'cody', 'dariel']
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


def make_users_follow_cashtags(cashtag_pk):
    cody_user = CashTagUser.objects.get(username='cody')
    dariel_user = CashTagUser.objects.get(username='dariel')

    neil_cashtag = CashTag.objects(creator_username='neil')[0]
    pk = str(neil_cashtag.pk)

    cody_user.cashtags_contributed_to.append(pk)
    dariel_user.cashtags_contributed_to.append(pk)
    cody_user.cashtags_watching.append(pk)

    cody_user.save()
    dariel_user.save()


def get_user_cashtags(username, num_active, num_contrib, num_watching):
    user = CashTagUser.objects.get(username=username)

    active_cashtags = user.cashtags_created_active
    contributed_cashtags = user.cashtags_contributed_to
    watching_cashtags = user.cashtags_watching

    assert len(active_cashtags) == num_active
    assert len(contributed_cashtags) == num_contrib
    assert len(watching_cashtags) == num_watching
    print('User cashtag tests passed for user ' + username)


if __name__ == '__main__':
    connect_to_mongodb_if_not_connected()
    drop_dat_db()

    create_test_users()
    verify_test_users()

    pk = post_cashtag()
    get_posted_cashtag(pk)

    make_users_follow_cashtags(pk)
    get_user_cashtags('neil', 1, 0, 0)
    get_user_cashtags('cody', 0, 1, 1)
    get_user_cashtags('dariel', 0, 1, 0)

