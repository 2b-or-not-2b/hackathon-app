import requests

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



if __name__ == '__main__':
    pk = post_cashtag()
    get_posted_cashtag(pk)


