from typing import List
from datetime import datetime, date
from pydantic import BaseModel as PyBaseModel, EmailStr, validator
from schemas.iquery_params import SortOrder, SortUserBy

from schemas.iuser_details import IUserDetail


class IUser(PyBaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    user_name: str
    email: EmailStr
    password: str
    birthday: date
    status: bool = True
    access: int | None = 1
    job_description: str
    personal_detail: IUserDetail | None = None

    @validator("first_name")
    @classmethod
    def validate_first_name(cls, value):
        return value.strip().upper()

    @validator("last_name")
    @classmethod
    def validate_last_name(cls, value):
        return value.strip().upper()

    @validator("middle_name")
    @classmethod
    def validate_middle_name(cls, value):
        return value and value.strip().upper()


class IUserOut(PyBaseModel):
    user_id: int
    first_name: str
    last_name: str
    middle_name: str | None = None
    user_name: str
    email: EmailStr
    birthday: date
    status: bool = True
    access: int | None = 1
    job_description: str
    last_updated: datetime | None
    date_created: datetime | None
    createdby: int
    last_updatedby: int


class IUserDetailOut(PyBaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    user_name: str
    email: EmailStr
    birthday: date
    status: bool = True
    access: int | None = 1
    job_description: str
    last_updated: datetime | None
    date_created: datetime | None
    createdby: int
    personal_detail: IUserDetail


class IUserUpdate(PyBaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    email: EmailStr | None = None
    birthday: date | None = None
    status: bool | None = None
    access: int | None = None
    job_description: str | None = None
    personal_detail: IUserDetail | None = None


class IUserQueryParams(PyBaseModel):
    name: str | None = None
    limit: int | None = 100
    sort_by: List[SortUserBy] | None = None
    skip: int | None = 0
    order: SortOrder | None = SortOrder.asc
