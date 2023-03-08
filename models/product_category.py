from datetime import datetime
from peewee import CharField, TextField,\
    AutoField, TimestampField, ForeignKeyField

from models.product import User
from models.base_model import BaseModel, database


class ProductCategory(BaseModel):
    category_id = AutoField()
    category_name = CharField(100, unique=True, index=True)
    description = TextField(null=True, default=None)
    createdby = ForeignKeyField(User, backref="productcatogries", index=True)
    date_created = TimestampField(default=datetime.now)


def create_product_category_table():
    with database:
        database.create_tables([ProductCategory])


def drop_product_category_table():
    with database:
        database.drop_tables([ProductCategory])
