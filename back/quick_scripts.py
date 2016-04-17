import requests
from decimal import Decimal
from mongoengine import DoesNotExist

from cashtag.models import CashTag, Contribution
from users.models import CashTagUser
from util.mongo_utils import connect_to_mongodb_if_not_connected

__author__ = '2b||!2b'

API_URL = 'http://45.55.34.6/api/'
# API_URL = 'http://localhost:8000/api/'


def drop_dat_db():
    for cash_tag in CashTag.objects():
        cash_tag.delete()
    for cash_tag_user in CashTagUser.objects():
        cash_tag_user.delete()
    for contrib in Contribution.objects():
        contrib.delete()


def post_cashtag():
    print('POSTing cashtag')
    data = {
        'creator_username': 'neil',
        'tag_name': '#emergecashtag',
        'title': 'Help Fund Our App',
        'min_price': '1',
        'tag_type': 'support',
        'description_txt': 'Help fund our app!\nTurn our hackathon entry into something bigger!!',
        'video': '',
        'image': 'img/open_source_library.png',
        'rewards': '',
    }

    response = requests.post(url='{}cashtag'.format(API_URL), json=data)
    print(response)
    assert response.ok
    assert response.status_code == 201
    return response.json()['_id']


def get_posted_cashtag(pk):
    print('GETing {}'.format(pk))
    response = requests.get(url='{}cashtag/.format(API_URL)?pk={}'.format(pk))
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

    user_info = ['neil', 'cody', 'dariel', 'ben', 'mike']
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
                money_able_to_send=100,
                avatar_img_url='img/{}.jpg'.format(username)
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
        try:
            assert len(user.contacts) == 3
        except AssertionError:
            print('len(user.contacts) ==')
            print(len(user.contacts))
    print('User creatiom verified')


def make_users_follow_cashtags(cashtag_pk):
    cody_user = CashTagUser.objects.get(username='cody')
    dariel_user = CashTagUser.objects.get(username='dariel')

    cody_user.contribute_to(cashtag_pk=cashtag_pk, amount=20)
    cody_user.contribute_to(cashtag_pk=cashtag_pk, amount=30)
    dariel_user.contribute_to(cashtag_pk=cashtag_pk, amount=100)
    dariel_user.stop_watching(cashtag_pk=cashtag_pk)

    cody_user.save()
    dariel_user.save()


def get_user_cashtags(username, num_active, num_contrib, num_watching, money_left):
    user = CashTagUser.objects.get(username=username)

    active_cashtags = user.cashtags_created_active
    contributed_cashtags = user.cashtags_contributed_to
    watching_cashtags = user.cashtags_watching

    assert len(active_cashtags) == num_active
    assert len(Contribution.objects(username=username)) == num_contrib
    assert len(watching_cashtags) == num_watching
    assert user.money_able_to_send == Decimal(money_left)

    print('User cashtag tests passed for user ' + username)


def create_more_sample_cashtags():
    data = {
        'creator_username': 'cody',
        'tag_name': '#big_party_miami2016',
        'title': 'Turn Down For What?!?!',
        'min_price': '1',
        'tag_type': 'support',
        'description_txt': 'Hi guys, we are hosting a big party. Beers included, the minimum support is just 10 bucks.',
        'video': '',
        'image': 'img/miami_party.jpg',
        'rewards': '',
    }
    response = requests.post(url='{}cashtag'.format(API_URL), json=data)
    assert response.ok
    assert response.status_code == 201

    data = {
        'creator_username': 'dariel',
        'tag_name': '#garage_sale_brickell',
        'title': 'Brickell Garage Sale',
        'min_price': '1',
        'tag_type': 'support',
        'description_txt': "Looking to sell old goods I don't need anymore",
        'video': '',
        'image': 'img/garage-sale.jpg',
        'rewards': '',
    }
    response = requests.post(url='{}cashtag'.format(API_URL), json=data)
    assert response.ok
    assert response.status_code == 201

    data = {
        'creator_username': 'ben',
        'tag_name': '#315ne2ave-rent',
        'title': 'Pay Rent for 315 ne 2nd ave',
        'min_price': '1',
        'tag_type': 'support',
        'description_txt': 'Home renters at 315 ne 2nd ave, you can pay your monthly rent here.',
        'video': '',
        'image': 'img/apartment-building.jpg',
        'rewards': '',
    }
    response = requests.post(url='{}cashtag'.format(API_URL), json=data)
    assert response.ok
    assert response.status_code == 201

    data = {
        'creator_username': 'mike',
        'tag_name': '#mywedding',
        'title': 'Happy Forever',
        'min_price': '10',
        'tag_type': 'support',
        'description_txt': "Hi friends, we're here to announce our wedding.\nPlease help us in funding this event. We hope to make this day special not just for us, but for you too.",
        'video': '',
        'image': 'img/wedding.jpg',
        'rewards': '',
    }
    response = requests.post(url='{}cashtag'.format(API_URL), json=data)
    assert response.ok
    assert response.status_code == 201
    print('created sample data')


if __name__ == '__main__':
    connect_to_mongodb_if_not_connected()
    drop_dat_db()

    create_test_users()
    verify_test_users()

    pk = post_cashtag()
    get_posted_cashtag(pk)

    make_users_follow_cashtags(pk)
    get_user_cashtags('neil', 1, 0, 0, 100)
    get_user_cashtags('cody', 0, 2, 1, 50)
    get_user_cashtags('dariel', 0, 1, 0, 0)

    create_more_sample_cashtags()

