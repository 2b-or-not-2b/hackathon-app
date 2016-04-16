import mongoengine


class CashTagUser(mongoengine.Document):
    username = mongoengine.StringField()
    password = mongoengine.StringField()

    cashtags_contributed_to = mongoengine.ListField()
    cashtags_watching = mongoengine.ListField()
    cashtags_created_active = mongoengine.ListField()
    # cashtags_created_past = mongoengine.ListField()

    friends = mongoengine.ListField()
    contacts = mongoengine.ListField()
