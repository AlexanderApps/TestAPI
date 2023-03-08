from peewee import Model, CharField, TextField, \
    DateField, IntegerField, FloatField, AutoField, BooleanField, \
    SmallIntegerField, TimestampField, ForeignKeyField


from models.user import User
from models.base_model import BaseModel, database


class UserDetail(BaseModel):
    user_id = ForeignKeyField(User, backref="users", index=True)
    user_phone = CharField(null=True)
    user_address = CharField(null=True)
    user_parent_name = CharField(null=True)
    bank_account_name = CharField(null=True)
    bank_account_number = CharField(null=True)
    bank_name = CharField(null=True)
    bank_branch = CharField(null=True)
    next_of_kin_name = CharField(null=True)
    next_of_kin_email = CharField(null=True)
    next_of_kin_number = CharField(null=True)
    next_of_kin_address = CharField(null=True)


def create_user_detail_table():
    with database:
        database.create_tables([UserDetail])


def drop_user_detail_table():
    with database:
        database.drop_tables([UserDetail])
