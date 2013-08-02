# -*- coding: UTF-8 -*-
import datetime

class Node(object):
    """
    this class represent an object (draw in dashed line) in work flow DAG.
    """

    def __init__(self, name, description, target):
        """
        :param name: name of the node
        :param description: description of the node
        :param target: target of the node
        """
        self.name = name
        self.description = description
        self.target = target

    @property
    def events(self):
        """
        :rtype: a list of :py:class:`work_flow_repr.Event`
        """
        return NotImplemented

    @property
    def children_groups(self):
        """
        return a groups of children
        
        :return: a list of children groups, each group should have 2 attributes:
            
                * name  - name of the group
                * items - children objects 
        """
        return NotImplemented

    @property
    def _processed_events(self):
        return sorted((e for e in self.events if e.datetime), key=lambda x: x.datetime or datetime.datetime.now())

    @property
    def json(self):
        """
        represent a tree root from self

        :rtype: DictType
        """
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
