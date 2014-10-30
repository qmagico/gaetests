import json
from google.appengine.ext import ndb


class AModel(ndb.Model):
    creation = ndb.DateTimeProperty(auto_now_add=True)
    data = ndb.TextProperty()

    def to_dict_json(self):
        d = json.loads(self.data)
        if self.creation:
            d['creation'] = self.creation.strftime('%Y/%m/%d %H:%M')
        return d