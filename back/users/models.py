import json

import mongoengine


class CashTagUser(mongoengine.Document):
    username = mongoengine.StringField()
    password = mongoengine.StringField()
    avatar_img_url = mongoengine.StringField()

    cashtags_contributed_to = mongoengine.ListField()
    cashtags_watching = mongoengine.ListField()
    cashtags_created_active = mongoengine.ListField()
    # cashtags_created_past = mongoengine.ListField()

    friends = mongoengine.ListField()
    contacts = mongoengine.ListField()

    money_able_to_send = mongoengine.DecimalField(default=0)
    money_pending = mongoengine.DecimalField(default=0)

    def to_api_json(self, json_dumps=False):
        data = {
            'username': self.username,
            'avatar_img_url': self.avatar_img_url,
            'cashtags_contributed_to': self.cashtags_contributed_to,
            'cashtags_watching': self.cashtags_watching,
            'cashtags_created_active': self.cashtags_created_active,
            'friends': self.friends,
            'contacts': self.contacts,
            'money_able_to_send': self.money_able_to_send,
            'money_pending': self.money_pending,
        }
        if json_dumps:
            return json.dumps(data)
        return data
