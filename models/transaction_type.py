from datetime import datetime
from peewee import CharField, TextField,\
    AutoField, SmallIntegerField, TimestampField

from models.base_model import BaseModel, database


class TransactionType(BaseModel):
    type_id = AutoField(index=True)
    type_name = CharField(100, unique=True, index=True)
    description = TextField(null=True, default=None)
    mod = SmallIntegerField()
    date_created = TimestampField(default=datetime.now)


def create_transaction_type_table():
    with database:
        database.create_tables([TransactionType])


def drop_transaction_type_table():
    with database:
        database.drop_tables([TransactionType])
