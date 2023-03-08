from typing import List, Optional, Union
from datetime import datetime, date, time
from pydantic import BaseModel as PyBaseModel, EmailStr
from schemas.iquery_params import SortOrder, SortUserBy

from schemas.iuser_details import IUserDetail


class IUser(PyBaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    user_name: str
    email: EmailStr
    password: str
    birthday: date
    status: bool = True
    access: Optional[int] = 1
    job_description: str
    personal_detail: Optional[IUserDetail] = None


class IUserOut(PyBaseModel):
    user_id: int
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    user_name: str
    email: EmailStr
    birthday: date
    status: bool = True
    access: Optional[int] = 1
    job_description: str
    last_updated: Optional[datetime]
    date_created: Optional[datetime]
    createdby: int
    last_updatedby: int


class IUserDetailOut(PyBaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    user_name: str
    email: EmailStr
    birthday: date
    status: bool = True
    access: Optional[int] = 1
    job_description: str
    last_updated: Optional[datetime]
    date_created: Optional[datetime]
    createdby: int
    personal_detail: IUserDetail


class IUserUpdate(PyBaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    email: Optional[EmailStr] = None
    birthday: Optional[date] = None
    status: Optional[bool] = None
    access: Optional[int] = None
    job_description: Optional[str] = None
    personal_detail: Optional[IUserDetail] = None


class IUserQueryParams(PyBaseModel):
    name: Optional[str] = None
    limit: Optional[int] = 100
    sort_by: Optional[List[SortUserBy]] = None
    skip: Optional[int] = 0
    order: Optional[SortOrder] = SortOrder.asc
