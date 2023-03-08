from datetime import datetime
from peewee import CharField, TextField, AutoField, TimestampField

from models.base_model import BaseModel, database


class Access(BaseModel):
    row_id = AutoField(index=True)
    access_name = CharField(100, unique=True)
    description = TextField(null=True, default=None)
    date_created = TimestampField(default=datetime.now)


def create_access_table():
    with database:
        database.create_tables([Access])


def drop_access_table():
    with database:
        database.drop_tables([Access])
