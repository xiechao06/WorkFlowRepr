# -*- coding: UTF-8 -*-
class Event(object):
    def __init__(self, datetime, name, actor, description='', by=''):
        self.datetime = datetime
        self.name = name
        self.actor = actor
        self.description = description
        self.by = by

    @property
    def json(self):
        ret = {
            'datetime': self.datetime.strftime("%Y-%m-%dT%H:%M:%S"),
            'name': self.name,
            'actor': self.actor,
            'description': self.description,
            'by': self.by,
        }
        return ret


