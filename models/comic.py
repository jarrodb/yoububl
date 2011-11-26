import datetime
import re
from mongokit import Document


class Caption(Document):
    __database__ = 'yoububl'
    __collection__ = 'comic'

    structure = {
        'title': unicode,
        'coords': unicode,
        'shape': unicode,
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


class Comic(Document):
    __database__ = 'yoububl'
    __collection__ = 'comic'

    structure = {
        'title': unicode,
        'file': unicode,
        'create_date': datetime.datetime,
        'captions': [Caption],
        'enabled': bool,
    }

    validators = {
    }

    default_values = {
        'create_date': datetime.datetime.utcnow,
        'enabled': False,
    }

    use_dot_notation = True

    indexes = [
        {'fields': ['title']},
    ]


ipaddr_re = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

class Vote(Document):
    structure = {
        'up': bool,
        'ipaddr': unicode,
    }

    validators = {
        'ipaddr': lambda x: ipaddr_re.match(x),
    }

    default_values = {
        'up': True,
    }

    use_dot_notation = True

    indexes = [
        {'fields': ['ipaddr']},
    ]


class UserCaption(Document):
    structure = {
        'comic': Comic,
        'votes': [Vote],
        'flagged': bool,
    }

    default_values = {
        'flagged': False,
    }

    use_dot_notation = True
    use_autorefs = True

    indexes = [
    ]
