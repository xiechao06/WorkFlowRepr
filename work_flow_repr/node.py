# -*- coding: UTF-8 -*-
import datetime
class Node(object):

    def __init__(self, name, description, target):
        self.name = name
        self.description = description
        self.target = target

    @property
    def events(self):
        return NotImplemented

    @property
    def children_groups(self):
        return NotImplemented

    @property
    def _processed_events(self):
        return sorted((e for e in self.events if e.datetime), key=lambda x: x.datetime or datetime.datetime.now())

    @property
    def json(self):
        ret = {
            'name': self.name,
            'target': self.target,
            'description': self.description,
            'events': [event.json for event in self._processed_events],
            'childrenGroups': [{
                'name': group.name,
                'items': [item.json for item in group.items]
            } for group in self.children_groups],
        }
        return ret
