import json
from datetime import datetime
import mongoengine

from users.models import CashTagUser

__author__ = '2b||!2b'


class Contribution(mongoengine.Document):
    username = mongoengine.StringField()
    amount = mongoengine.DecimalField()
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

    """{
            'name': <string>,
            'avatar': <url>,
            'amount': <string>('$25' || 'Private
    }"""

    def validate_cashtag(self):
        print('validating cashtag {}'.format(self.title))
        if not self.description_html:
            self.description_html = '<div>{}</div>'.format(self.description_txt.replace('\n', '<br/>'))

            self.tag_name = self.title + '-' + self.creator_username
        if not self.min_price:
            self.min_price = 0

        self.creation_timestamp = datetime.now()
        return True

    def to_api_json(self, json_dumps=False):
        def api_json_supporter(username):
            user = CashTagUser.objects.get(username=username)
            return {
                'username': user.username,
                'avatar': user.avatar,
                'amount': CashTagUser.get_user_contributions_total(username=username, cashtag_pk=self.pk),
            }

        try:
            data = {
                '_id': str(self.pk),
                'creator_username': self.creator_username,
                'money_collected': self.money_collected,
                'tag_name': self.tag_name,
                'title': self.title,
                'min_price': self.min_price,
                'tag_type': self.tag_type,
                'description_txt': self.description_txt,
                'description_html': self.description_html,
                'creation_timestamp': self.creation_timestamp.isoformat() if self.creation_timestamp else None,
                'video': self.video,
                'image': self.image,
                'rewards': self.rewards,
                'supporters': [api_json_supporter(username) for username in self.supporters]
            }
            if json_dumps:
                return json.dumps(data)
            return data
        except Exception as e:
            print(e)
            raise
