import csv
import random
from datetime import date
from typing import Optional
from string import ascii_letters
from pydantic import BaseModel as PyBaseModel, EmailStr

from models.user import User
from models.state import Status
from models.access import Access
from auth.oauth import password_hasher
from models.base_model import database
from models.transaction_type import TransactionType


####################################
# generating tep password for admin
####################################


def temp_rand():
    result = (
        "".join(
            random.choice(
                ascii_letters +
                "0123456789"
            ) for i in range(9))
    )
    if True: # ideally DEV ENV
        result = "password"
    return result


def send_temp_password(user: dict):
    password = temp_rand()
    user["password"] = password_hasher(password)
    print(
        f"Sending Temp Password Via Email: \nEmail: {user['email']} \nTemp Password: {password}")
    return user


##################################
# intialize access table
##################################


class AccessInit(PyBaseModel):
    access_name: str
    description: Optional[str] = None


def init_access():
    with open("data/init_access.csv", "r") as f:
        data = csv.DictReader(f)
        rows = map(lambda d: AccessInit(**d).dict(), data)
        q = Access.insert_many([row for row in rows]).execute()


# ##################################
# # intialize transaction type table
# ##################################


class TransactionTypeInit(PyBaseModel):
    type_name: str
    description: Optional[str] = None
    mod: int


def init_transaction_type():
    with open("data/init_transactype.csv", "r") as f:
        data = csv.DictReader(f)
        rows = map(lambda e: TransactionTypeInit(**e).dict(), data)
        q = TransactionType.insert_many([row for row in rows]).execute()


# ##################################
# # intialize status table
# ##################################


class StatusInit(PyBaseModel):
    status_name: str
    status: int
    description: Optional[str] = None


def init_status():
    with open("data/init_status.csv", "r") as f:
        data = csv.DictReader(f)
        rows = map(lambda e: StatusInit(**e).dict(), data)
        q = Status.insert_many([row for row in rows]).execute()


# ##################################
# # intialize user table
# ##################################

class UserInit(PyBaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: EmailStr
    birthday: date
    status: int
    access: int
    job_description: str


def update_creators(u):
    u.createdby = 1
    u.last_updatedby = 1
    return u


@database.atomic()
def init_admin():
    with open("data/init_user.csv", "r") as f:
        data = csv.DictReader(f)
        rows = map(lambda e: UserInit(**e).dict(), data)
        _rows = map(send_temp_password, rows)
        q = User.insert_many(_rows).execute()
        u = map(update_creators, User.select())
        User.bulk_update([x for x in u], fields=[
                         User.last_updatedby, User.createdby])
