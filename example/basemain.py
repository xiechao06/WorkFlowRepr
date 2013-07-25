#! # -*- coding: UTF-8 -*-
from collections import namedtuple
from datetime import datetime

from flask import Flask, render_template
from work_flow_repr import Node, Event

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///temp.db"
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

@app.route('/svg1')
def svg1():
    class OrderNode(Node):

        @property
        def events(self):
            return [
                Event(datetime.strptime('2013-07-22T15:35:00', "%Y-%m-%dT%H:%M:%S"), u'生成订单', 'cc', '生成订单的描述', '生成订单'),
                Event(datetime.strptime('2013-07-22T15:40:00', "%Y-%m-%dT%H:%M:%S"), u'下发订单', 'cc', '开始下发订单的描述', ''),
            ]

        @property
        def children_groups(self):
            return []

    class ReceiptNode(Node):
        @property
        def events(self):
            return [
                Event(datetime.strptime('2013-07-22T14:33:00', "%Y-%m-%dT%H:%M:%S"), u'开始卸货', 'cc', '开始卸货的描述', ''),
                Event(datetime.strptime('2013-07-22T15:33:00', "%Y-%m-%dT%H:%M:%S"), u'卸货完毕', 'cc', '卸货完毕的描述', ''),
                Event(datetime.strptime('2013-07-22T15:35:00', "%Y-%m-%dT%H:%M:%S"), u'生成订单', 'cc', '生成订单的描述', ''),
            ]


        @property
        def children_groups(self):
            ChildrenGroup = namedtuple('ChildrenGroup', ['name', 'items'])
            return [
                ChildrenGroup(u'订单', [OrderNode(u'订单A', u'订单A的描述', 'http://www.baidu.com'), OrderNode(u'订单A', u'订单A的描述', 'http://www.baidu.com')])
            ]
    
    receipt_node = ReceiptNode(u'收货单A', u'收货单A的描述', 'http://www.baidu.com') 

    return render_template('svg.html', tree=receipt_node.json)

@app.route('/svg2')
def svg2():
    from models import User, Customer, GoodsReceipt, Order
    from work_flow_repr.utils import annotate_model, ModelNode, make_tree

    class GoodsReceiptNode(ModelNode):

        @property
        def name(self):
            return u"收货单" + unicode(self.obj)

        @property
        def description(self):
            return 'this is GoodsReceipt %d' % self.obj.id

        @property
        def events(self):
            return [
                Event(self.obj.unload_time, u'unload start', self.obj.creator.username, 'unload start at ' + str(self.obj.unload_time), ''),
                Event(self.obj.unload_done_time, u'unload done', self.obj.creator.username, 'unload completed at ' + str(self.obj.unload_done_time), ''),
                Event(self.obj.order.create_time, u'generate order(s)', self.obj.creator.username, 'generate order at ' + str(self.obj.order.create_time), ''),
            ]

        @property
        def target(self):
            return 'http://www.baidu.com'

        @property
        def children_model_groups(self):
            return [('order', [self.obj.order]),]
            
    class OrderNode(ModelNode):

        @property
        def name(self):
            return u"订单" + unicode(self.obj)

        @property
        def description(self):
            return 'this is Order %d' % self.obj.id

        @property
        def target(self):
            return 'http://www.baidu.com'

        @property
        def events(self):
            return [
                Event(self.obj.create_time, 'generate', self.obj.creator.username, 'genreate at ' + str(self.obj.create_time), 'generate order(s)'),
                Event(self.obj.dispatch_time, 'dispatch', self.obj.creator.username, 'dispath at ' + str(self.obj.dispatch_time), ''),
            ]

        @property
        def children_model_groups(self):
            return [] 

    annotate_model(GoodsReceipt, GoodsReceiptNode)
    annotate_model(Order, OrderNode)
    return render_template('svg.html', tree=make_tree(GoodsReceipt.query.first()))

if __name__ == "__main__":
    app.run()
