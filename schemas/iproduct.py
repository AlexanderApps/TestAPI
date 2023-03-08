from datetime import date
from typing import Optional, List
from pydantic import BaseModel as PyBaseModel

from schemas.iquery_params import SortOrder, SortProductBy


class IProduct(PyBaseModel):
    name: str
    other_names: Optional[str] = None
    batch_number: Optional[str] = None
    expiry_date: date
    status: Optional[int] = 1
    access: Optional[int] = 1
    price: float
    quantity_available: int


class IProductUpdate(PyBaseModel):
    product_id: int
    name: Optional[str] = None
    batch_number: Optional[str] = None
    expiry_date: Optional[date] = None
    access: Optional[int] = None
    status: Optional[int] = None
    price: Optional[float] = None
    # quantity_available: Optional[int] = None


class IProductQueryParams(PyBaseModel):
    name: Optional[str] = None
    limit: Optional[int] = 100
    sort_by: Optional[List[SortProductBy]] = None
    skip: Optional[int] = 0
    order: Optional[SortOrder] = SortOrder.asc
    expired: Optional[bool] = None
