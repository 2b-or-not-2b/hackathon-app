import mongoengine


# Create your models here.
class CashTagUser(mongoengine.Document):
    username = mongoengine.StringField()
    password = mongoengine.StringField()

