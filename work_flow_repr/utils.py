# -*- coding: UTF-8 -*-
from collections import namedtuple
from work_flow_repr import Node

_table_model_spec_map = {}

def annotate_model(model, node_cls):
    """
    annotate the model, tell WFR that the model should be represented using 'node_cls'

    :param model: a model **CLASS** which is defined in Sqlalchemy's *Declarative* way 
    :param node_cls: a node **CLASS**
    :type node_cls: :py:class:`work_flow_repr.Node`

    """
    _table_model_spec_map[model.__tablename__] = node_cls


class ModelNode(Node):
    """
    A helpler class to generate Node from model. to draw a work flow DAG:
        
        * you **MUST** implement :py:meth:`~ModelNode.children_model_groups`
        * you **SHOULD** override description :py:meth:`~ModelNode.description`, :py:meth:`~ModelNode.target`
        * you **MAY** override :py:meth:`ModelNode.name`

    .. code-block:: python
        
        class Order(db.Model):
            __tablename__ = 'TB_ORDER'

            id = db.Column(db.Integer, primary_key=True)

        class WorkCommand(db.Model):
            __tablename__ = 'TB_WORK_COMMAND'

            id = db.Column(db.Integer, primary_key=True)
            order_id = db.Column(db.Integer, db.ForeignKey("TB_ORDER.id"))
            order = db.relationship("Order", backref='work_command_list')

        class OrderModelNode(ModelNode):

            @property
            def description(self):
                return 'an <strong>order</strong> is a commitment made to customer'

            @property
            def target(self):
                return '/order/' + str(self.obj.id)

            @property
            def events(self):
                return [
                    Event(datetime.strptime('2013-08-01 10:00:00', "%Y-%m-%d %H:%M:%S"), 'create', 'manager'),
                    Event(datetime.strptime('2013-08-01 10:30:00', "%Y-%m-%d %H:%M:%S"), 'split to work commands', 'manager'),
                ]

            @property
            def children_model_groups(self):
                return [('work command list', self.obj.work_command_list)]

        class WorkCommandModelNode(ModelNode):
            
            @property
            def children_model_groups(self):
                return []

            @property
            def target(self):
                return '/work_command/' + str(self.obj.id)

            @property
            def events(self):
                return [
                    Event(datetime.strptime('2013-08-01 10:30:00', "%Y-%m-%d %H:%M:%S"), 'create', 'worker', by='split to work command'),
                    Event(datetime.strptime('2013-08-01 17:30:00', "%Y-%m-%d %H:%M:%S"), 'finish', 'worker'),
                ]

            @property
            def name(self):
                return 'WC'

        annotate(Order, OrderModelNode)
        annotate(WorkCommand, WorkCommandModelNode)
    """

    def __init__(self, obj):
        """
        :param obj: a model object 
        """
        self.obj = obj

    @property
    def name(self):
        '''
        name of the node
        '''
        return unicode(self.obj)

    @property
    def description(self):
        """
        description of the object
        """
        return ''

    @property
    def target(self):
        """
        the url of the model object's detail page
        """
        return ''

    @property
    def children_groups(self):
        """
        see :py:meth:`work_flow_repr.Node.children_groups`
        """
        ChildrenGroup = namedtuple('ChildrenGroup', ['name', 'items'])
        ret = []
        for group_name, group in self.children_model_groups:
            ret.append(ChildrenGroup(group_name, [_table_model_spec_map[obj.__tablename__](obj) for obj in group]))
        return ret

    @property
    def children_model_groups(self):
        """
        :return: groups of models, each group is a tuple of 2 elements, first is the name of the group, second is the
            object of the groups
        :rtype: list of tuples
        """
        return NotImplemented


def make_tree(obj):
    """
    make a tree whose root is 'obj', see :py:meth:`work_flow_repr.Node.json`

    :param obj: a model object, the model should be annotated by :py:func:`work_flow_repr.utils.annotate_model`
    :return: a tree whose root is 'obj'
    :type: DictType
    
    """
    return _table_model_spec_map[obj.__tablename__](obj).json
