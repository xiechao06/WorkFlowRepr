# -*- coding: UTF-8 -*-
class Event(object):
    """
    represent an event in work flow DAG
    """

    def __init__(self, datetime, name, actor, description='', by=''):
        """

        :param datetime: datetime of the event
        :type datetime: datetime.datetime
        :param name: name of the event
        :param actor: the actor of the event
        :param description: description of the event
        :by: if the event is the birth event of a node, and the node is generated by another node's event (say branch event), 
            then by should be the name of the branch event

        """
        self.datetime = datetime
        self.name = name
        self.actor = actor
        self.description = description
        self.by = by

    @property
    def json(self):
        '''
        represent the event as dict

        :rtype: DictType

        '''
        ret = {
            'datetime': self.datetime.strftime("%Y-%m-%dT%H:%M:%S"),
            'name': self.name,
            'actor': self.actor,
            'description': self.description,
            'by': self.by,
        }
        return ret


