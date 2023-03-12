from peewee import TextField, AutoField, TimestampField

from models.base_model import BaseModel, database


class LoginBlacklist(BaseModel):
    row_id = AutoField()
    token = TextField(unique=True)
    expiry = TimestampField()


def create_accesslogin_backlist_table():
    with database:
        database.create_tables([LoginBlacklist])


def drop_login_blacklist_table():
    with database:
        database.drop_tables([LoginBlacklist])
