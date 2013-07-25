# -*- coding: UTF-8 -*-
from collections import namedtuple
from work_flow_repr import Node

_table_model_spec_map = {}

def annotate_model(model, node_cls):
    _table_model_spec_map[model.__tablename__] = node_cls

class ModelNode(Node):

    def __init__(self, obj):
        self.obj = obj

    @property
    def name(self):
        return unicode(self.obj)

    @property
    def description(self):
        return ''

    @property
    def target(self):
        return ''

    @property
    def children_groups(self):
        ChildrenGroup = namedtuple('ChildrenGroup', ['name', 'items'])
        ret = []
        for group_name, group in self.children_model_groups:
            ret.append(ChildrenGroup(group_name, [_table_model_spec_map[obj.__tablename__](obj) for obj in group]))
        return ret

    @property
    def children_model_groups(self):
        return NotImplemented

def make_tree(obj):
    return _table_model_spec_map[obj.__tablename__](obj).json
