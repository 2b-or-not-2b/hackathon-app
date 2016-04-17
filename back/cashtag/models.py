import json
from datetime import datetime
import mongoengine
from mongoengine import DoesNotExist

from users.models import CashTagUser

__author__ = '2b||!2b'


class Contribution(mongoengine.Document):
    username = mongoengine.StringField()
    amount = mongoengine.DecimalField()
    cashtag_pk = mongoengine.StringField()
    notes = mongoengine.StringField()
    timestamp = mongoengine.DateTimeField()


class CashTag(mongoengine.Document):
    creator_username = mongoengine.StringField()
    money_collected = mongoengine.DecimalField(min_value=0, default=0)
    tag_name = mongoengine.StringField()
    title = mongoengine.StringField()
    min_price = mongoengine.IntField()
    tag_type = mongoengine.StringField()
    description_txt = mongoengine.StringField()
    description_html = mongoengine.StringField()
    creation_timestamp = mongoengine.DateTimeField()
    video = mongoengine.StringField()
    image = mongoengine.StringField()
    rewards = mongoengine.ListField()
    supporters = mongoengine.ListField()
    days_to_live = mongoengine.IntField(default=30)
    int_id = mongoengine.IntField()

    """{
            'name': <string>,
            'avatar': <url>,
            'amount': <string>('$25' || 'Private
    }"""

    def validate_cashtag(self):
        print('validating cashtag {}'.format(self.title))
        if not self.description_html:
            self.description_html = '<div>{}</div>'.format(self.description_txt.replace('\n', '<br/>'))

            # self.tag_name = self.title + '-' + self.creator_username
        if not self.min_price:
            self.min_price = 0

        self.creation_timestamp = datetime.now()
        return True

    def to_api_json(self, json_dumps=False):
        def api_json_supporter(username):
            user = CashTagUser.objects.get(username=username)
            return {
                'username': user.username,
                'avatar_img_url': user.avatar_img_url,
                'amount': CashTagUser.get_user_contributions_total(username=username, cashtag_pk=self.pk),
            }

        try:
            tag_name_no_hash = str(self.tag_name)
            user_avatar_img_url = ''
            if tag_name_no_hash[0] == '#':
                tag_name_no_hash = tag_name_no_hash[1:]
            try:
                user = CashTagUser.objects.get(username=self.creator_username)
                user_avatar_img_url = user.avatar_img_url
            except DoesNotExist:
                pass

            data = {
                'id': self.int_id,
                '_id': str(self.pk),
                'creator_username': self.creator_username,
                'raised_money': self.money_collected,
                'tag_name': self.tag_name,
                'title': self.title,
                'price': self.min_price,
                'tag_type': self.tag_type,
                'desc': self.description_txt,
                'description_html': self.description_html,
                'creation_timestamp': self.creation_timestamp.isoformat() if self.creation_timestamp else None,
                'video': self.video,
                'image': self.image,
                'rewards': self.rewards,
                'supporters': [api_json_supporter(username) for username in self.supporters],
                'share_url': 'http://45.55.34.6/share/' + tag_name_no_hash,
                'face': user_avatar_img_url
            }
            if json_dumps:
                return json.dumps(data)
            return data
        except Exception as e:
            print(e)
            raise
