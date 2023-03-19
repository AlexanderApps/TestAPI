from peewee import TextField, ForeignKeyField, TimestampField

from models.base_model import BaseModel, database
from models.user import User


class LoginRefreshToken(BaseModel):
    row_id = ForeignKeyField(User, backref="users", index=True)
    token = TextField(unique=True)
    expiry = TimestampField()


def create_login_refresh_token_table():
    with database:
        database.create_tables([LoginRefreshToken])


def drop_login_refresh_token_table():
    with database:
        database.drop_tables([LoginRefreshToken])
