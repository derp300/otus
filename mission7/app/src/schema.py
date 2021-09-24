import enum

from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import DateTime, Enum
from sqlalchemy.sql import func


db = SQLAlchemy()


class Order(db.Model):
    __tablename__ = "myorder"

    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer())
    price = db.Column(db.Integer())
    created = db.Column(DateTime(timezone=True), server_default=func.now())
    updated = db.Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __init__(self, count, price):
        self.count = count
        self.price = price

    def __repr__(self):
        return f"{self.count} ({self.price})"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class OrderSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Order
        sqla_session = db.session

    count = fields.String(required=True)
    price = fields.String(required=True)

