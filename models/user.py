from datetime import datetime
from peewee import CharField, TextField, DateField, \
    AutoField, TimestampField, ForeignKeyField

from models.state import Status
from models.access import Access
from models.base_model import BaseModel, database


class User(BaseModel):
    user_id = AutoField()
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, null=True, default=None)
    user_name = CharField(max_length=5, unique=True, index=True)
    password = TextField()
    email = TextField(unique=True)
    birthday = DateField(formats=["%Y-%m-%d"])
    status = ForeignKeyField(Status, backref="users", index=True)
    access = ForeignKeyField(Access, backref="users", index=True)
    job_description = TextField()
    last_updated = TimestampField(default=datetime.now)
    date_created = TimestampField(default=datetime.now)
    createdby = ForeignKeyField(
        'self', backref="children", null=True, index=True)
    last_updatedby = ForeignKeyField(
        'self', backref="children", null=True, index=True)


def create_user_table():
    with database:
        database.create_tables([User])


def drop_user_table():
    with database:
        database.drop_tables([User])
