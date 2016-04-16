import mongoengine

from users.models import CashTagUser

__author__ = '2b||!2b'


def connect_to_mongodb_if_not_connected():
    try:
        test = CashTagUser.objects.get(username='test_user')
    except mongoengine.connection.ConnectionError:
        _MONGODB_USER = ''
        _MONGODB_PASSWD = ''
        _MONGODB_HOST = 'localhost'
        _MONGODB_NAME = 'cashtag'
        if _MONGODB_USER or _MONGODB_PASSWD:
            _MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' \
                                     % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)
        else:
            _MONGODB_DATABASE_HOST = 'mongodb://%s/%s' \
                                     % (_MONGODB_HOST, _MONGODB_NAME)

        mongoengine.connect(_MONGODB_NAME, host=_MONGODB_DATABASE_HOST)


