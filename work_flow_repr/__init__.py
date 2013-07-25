# -*- coding: UTF-8 -*-

from .event import Event
from .node import Node

if __name__ == "__main__":
    
    class OrderNode(Node):

        @property
        def events(self):
            return [
                Event(datetime.strptime('2013-07-22T14:33:00', "%Y-%m-%dT%H:%M:%S"), u'开始卸货', 'cc', '开始卸货的描述', ''),
                Event(datetime.strptime('2013-07-22T15:33:00', "%Y-%m-%dT%H:%M:%S"), u'卸货完毕', 'cc', '卸货完毕的描述', ''),
                Event(datetime.strptime('2013-07-22T15:35:00', "%Y-%m-%dT%H:%M:%S"), u'生成订单', 'cc', '生成订单的描述', ''),
            ]

        @property
        def children_groups(self):
            return []

    class ReceiptNode(Node):

        @property
        def events(self):
            return [
                Event(datetime.strptime('2013-07-22T15:35:00', "%Y-%m-%dT%H:%M:%S"), u'生成订单', 'cc', '生成订单的描述', '生成订单'),
                Event(datetime.strptime('2013-07-22T15:40:00', "%Y-%m-%dT%H:%M:%S"), u'下发订单', 'cc', '开始下发订单的描述', ''),
            ]

        @property
        def children_groups(self):
            ChildrenGroup = namedtuple('ChildrenGroup', ['name', 'items'])
            return [
                ChildrenGroup(u'订单', [OrderNode(u'订单A', u'订单A的描述', 'http://www.baidu.com')])
            ]
    
    receipt_node = ReceiptNode(u'收货单A', u'收货单A的描述', 'http://www.baidu.com') 

    print receipt_node.json
