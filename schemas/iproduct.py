from datetime import date
from typing import List
from pydantic import BaseModel as PyBaseModel, validator

from schemas.iquery_params import SortOrder, SortProductBy


class IProduct(PyBaseModel):
    name: str
    other_names: str | None
    batch_number: str | None
    expiry_date: date
    status: int | None = 1
    access: int | None = 1
    price: float
    quantity_available: int

    @validator("name")
    @classmethod
    def validate_name(cls, value):
        return " ".join(v for v in value.strip().upper().split(" ") if v != "")

    @validator("other_names")
    @classmethod
    def validate_other_names(cls, value):
        return value.strip().upper()

    @validator("status")
    @classmethod
    def validate_status(cls, value):
        if value <= 0:
            raise ValueError("status cannot be less than or equal to 0.")
        return value

    @validator("access")
    @classmethod
    def validate_access(cls, value):
        if value <= 0:
            raise ValueError("access cannot be less than or equal to 0.")
        return value


class IProductUpdate(IProduct):
    name: str | None = None
    batch_number: str | None = None
    expiry_date: date | None = None
    access: int | None = None
    status: int | None = None
    price: float | None = None
    quantity_available: int | None = None


class IProductQueryParams(PyBaseModel):
    name: str | None = None
    limit: int | None = 100
    sort_by: List[SortProductBy] | None = None
    skip: int | None = 0
    order: SortOrder | None = SortOrder.asc
    expired: bool | None = None
