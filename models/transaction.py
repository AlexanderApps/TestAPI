from peewee import Model, CharField, TextField, \
    DateField, IntegerField, FloatField, AutoField, BooleanField, \
    SmallIntegerField, TimestampField, ForeignKeyField, DecimalField


from models.base_model import BaseModel, database
from models.user import User


class Transaction(BaseModel):
    transaction_id = AutoField()
    transaction_name = TextField(index=True, unique=True)
    type = SmallIntegerField()
    amount = DecimalField()
    status = SmallIntegerField()
    access = SmallIntegerField()
    last_updated = TimestampField()
    date_created = TimestampField()
    createdby = ForeignKeyField(User, backref="transactions", index=True)
    last_updatedby = ForeignKeyField(User, backref="transactions", index=True)


def create_transaction_table():
    with database:
        database.create_tables([Transaction])


def drop_transaction_table():
    with database:
        database.drop_tables([Transaction])
