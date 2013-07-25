# -*- coding: UTF-8 -*-
from datetime import datetime
from basemain import db

class Customer(db.Model):
    __modelname__ = u"客户"
    __tablename__ = "TB_CUSTOMER"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)

class GoodsReceipt(db.Model):
    __tablename__ = "TB_GOODS_RECEIPT"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('TB_CUSTOMER.id'))
    customer = db.relationship(Customer)
    create_time = db.Column(db.DateTime, default=datetime.now)
    order = db.relationship(
        "Order", backref=db.backref("goods_receipt", uselist=False),
        cascade="all, delete-orphan", uselist=False)
    unload_time = db.Column(db.DateTime)
    unload_done_time = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer, db.ForeignKey("TB_USER.id"))
    creator = db.relationship("User")

    def __unicode__(self):
        return unicode(self.id)

class Order(db.Model):
    __tablename__ = "TB_ORDER"

    id = db.Column(db.Integer, primary_key=True)
    goods_receipt_id = db.Column(db.Integer,
                                 db.ForeignKey('TB_GOODS_RECEIPT.id'))
    create_time = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer, db.ForeignKey("TB_USER.id"))
    creator = db.relationship("User")
    dispatch_time = db.Column(db.DateTime)

    def __unicode__(self):
        return unicode(self.id)

class User(db.Model):
    __tablename__ = "TB_USER"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
