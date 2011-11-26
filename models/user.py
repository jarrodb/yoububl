import datetime
import hashlib
import re

from mongokit import Document

class User(Document):
    __database__ = 'yoububl'
    __collection__ = 'user'

    structure = {
        'name': unicode,
        'username': unicode,
        'password': unicode,
    }

    validators = {
        'title': lambda x: re.match(r'^[\w\-\.]+$', x),
        'coords': lambda x: len(x.split(',')) == 4,
    }

    default_Values = {
        'shape': u'rect',
    }

    use_dot_notation = True
    use_autorefs = True

    indexes = [
        {'fields': ['title']},
    ]

    def set_password(self, password):
        hash_password = hashlib.md5(password).hexdigest()
        self.password = hash_password
        self.save()


