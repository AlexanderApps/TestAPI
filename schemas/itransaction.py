from datetime import datetime
from typing import List
from pydantic import BaseModel as PyBaseModel, validator
from schemas.iquery_params import SortOrder, SortTransactionBy

from schemas.itransaction_product import IProductTransaction


class ITransaction(PyBaseModel):
    transaction_name: str
    access: int | None = 1
    type: int
    status: int
    createdby: int
    last_updatedby: int
    items: List[IProductTransaction]
    amount: float

    @validator("transaction_name")
    @classmethod
    def validate_transaction_name(cls, value):
        return value.strip()


class ITransactionItems(PyBaseModel):
    name: str
    price: float
    quantity: int


class ITransactionBody(PyBaseModel):
    transaction_id: int
    transaction_name: str
    date_created: datetime
    amount: float
    type: int
    type_name: str
    user_name: str
    items: List[ITransactionItems]


class ITransactionQueryParams(PyBaseModel):
    name: str | None = None
    limit: int | None = 100
    sort_by: List[SortTransactionBy] | None = None
    skip: int | None = 0
    order: SortOrder | None = SortOrder.asc
