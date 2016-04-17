import json

import datetime
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
        from cashtag.models import CashTag

        friends = [CashTagUser.objects.get(pk=pk).username for pk in self.friends]
        contacts = [CashTagUser.objects.get(pk=pk).username for pk in self.contacts]
        data = {
            'username': self.username,
            'avatar_img_url': self.avatar_img_url,
            'cashtags_contributed_to': self.cashtags_contributed_to,
            'cashtags_watching': self.cashtags_watching,
            'cashtags_created_active': [CashTag.objects.get(pk=pk).to_api_json() for pk in self.cashtags_created_active],
            'friends': friends,
            'contacts': contacts,
            'money_able_to_send': self.money_able_to_send,
            'money_pending': self.money_pending,
        }
        if json_dumps:
            return json.dumps(data)
        return data

    @staticmethod
    def get_user_contributions_total(username, cashtag_pk):
        cashtag_pk = str(cashtag_pk)
        from cashtag.models import Contribution
        user_contributions = Contribution.objects(username=username, cashtag_pk=cashtag_pk)
        return sum(contrib.amount for contrib in user_contributions)

    def contribute_to(self, cashtag_pk, amount, notes=None):
        from cashtag.models import CashTag, Contribution
        assert amount > 0
        assert amount <= self.money_able_to_send

        cash_tag = CashTag.objects.get(pk=cashtag_pk)
        assert amount > cash_tag.min_price

        contribution = Contribution(
            username=self.username,
            amount=amount,
            cashtag_pk=cashtag_pk,
            notes=notes,
            timestamp=datetime.datetime.now(),
        )
        contribution.save()

        self.money_able_to_send -= amount
        if cashtag_pk not in self.cashtags_watching:
            # Don't re-follow if we've donated in the apst and explicitly stopped watching
            if cashtag_pk not in self.cashtags_contributed_to:
                self.cashtags_watching.append(cashtag_pk)
        if cashtag_pk not in self.cashtags_contributed_to:
            self.cashtags_contributed_to.append(cashtag_pk)
        self.save()

        cash_tag.money_collected += amount
        if self.username not in cash_tag.supporters:
            cash_tag.supporters.append(self.username)
        cash_tag.save()

    def stop_watching(self, cashtag_pk):
        if cashtag_pk in self.cashtags_watching:
            self.cashtags_watching.remove(cashtag_pk)
        self.save()




