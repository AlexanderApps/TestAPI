from datetime import datetime
from peewee import CharField, TextField, \
    DateField, IntegerField, AutoField,\
    TimestampField, ForeignKeyField, DecimalField

from models.user import User
from models.state import Status
from models.access import Access
from models.base_model import BaseModel, database


class Product(BaseModel):
    product_id = AutoField()
    name = CharField(max_length=100, index=True, unique=True)
    other_names = TextField(null=True, default=None)
    batch_number = CharField(max_length=50, null=True, default=None)
    status = ForeignKeyField(Status, backref="products", index=True)
    expiry_date = DateField(formats=["%Y-%m-%d"])
    access = ForeignKeyField(Access, backref="products", index=True)
    last_updated = TimestampField(default=datetime.now)
    date_created = TimestampField(default=datetime.now)
    createdby = ForeignKeyField(User, backref="products", index=True)
    last_updatedby = ForeignKeyField(User, backref="products", index=True)
    price = DecimalField(decimal_places=2, auto_round=True)
    quantity_available = IntegerField()


def create_product_table():
    with database:
        database.create_tables([Product])


def drop_product_table():
    with database:
        database.drop_tables([Product])
