# -*- coding: UTF-8 -*-
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
    def json(self):
        ret = {
            'name': self.name,
            'target': self.target,
            'description': self.description,
            'events': [event.json for event in sorted(self.events, key=lambda x: x.datetime)],
            'childrenGroups': [{
                'name': group.name,
                'items': [item.json for item in group.items]
            } for group in self.children_groups],
        }
        return ret
