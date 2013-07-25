# -*- coding: UTF-8 -*-

import types
from datetime import datetime
from basemain import db
from models import Customer, GoodsReceipt, Order, User

def do_commit(obj, action="add"):
    if action == "add":
        if isinstance(obj, types.ListType) or isinstance(obj, types.TupleType):
            db.session.add_all(obj)
        else:
            db.session.add(obj)
    elif action == "delete":
        db.session.delete(obj)
    db.session.commit()
    return obj

db.create_all()

user = do_commit(User(username=u"cargo clerk"))
customer = do_commit(Customer(name=u"CCTV"))
goods_receipt = do_commit(GoodsReceipt(customer=customer, unload_time=datetime.strptime("2013-07-22 12:22:23", "%Y-%m-%d %H:%M:%S"),
                           unload_done_time=datetime.strptime("2013-07-22 12:52:23", "%Y-%m-%d %H:%M:%S"), creator=user))
order = do_commit(Order(creator=user, goods_receipt=goods_receipt, create_time=datetime.strptime("2013-07-22 12:55:23", "%Y-%m-%d %H:%M:%S"),
                       dispatch_time=datetime.strptime("2013-07-22 13:00:23", "%Y-%m-%d %H:%M:%S")))

