from datetime import datetime
from peewee import CharField, TextField, \
    AutoField, BooleanField, TimestampField

from models.base_model import BaseModel, database


class Status(BaseModel):
    row_id = AutoField(index=True)
    status_name = CharField(100, unique=True)
    status = BooleanField()
    description = TextField(null=True, default=None)
    date_created = TimestampField(default=datetime.now)


def create_status_table():
    with database:
        database.create_tables([Status])


def drop_status_table():
    with database:
        database.drop_tables([Status])
