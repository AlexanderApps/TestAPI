from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel as PyBaseModel
from schemas.iquery_params import SortOrder, SortTransactionBy

from schemas.itransaction_product import IProductTransaction


class ITransaction(PyBaseModel):
    transaction_name: str
    type: Optional[int] = 1
    access: Optional[int] = 1
    status: int
    createdby: int
    last_updatedby: int
    items: List[IProductTransaction]
    amount: float


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
    name: Optional[str] = None
    limit: Optional[int] = 100
    sort_by: Optional[List[SortTransactionBy]] = None
    skip: Optional[int] = 0
    order: Optional[SortOrder] = SortOrder.asc
