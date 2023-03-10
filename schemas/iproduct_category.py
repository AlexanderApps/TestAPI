from typing import List, Optional
from pydantic import BaseModel as PyBaseModel

from schemas.iquery_params import SortOrder, SortProductCategoryBy


class IProductCategory(PyBaseModel):
    category_name: str
    description: Optional[str] = None


class IProductCategoryUpdate(PyBaseModel):
    category_name: Optional[str] = None
    description: Optional[str] = None


class IProductCategoryRef(PyBaseModel):
    category_id: int
    product_id: int


class IProductCategoryRefAdd(PyBaseModel):
    product_id: int


class IProductCategoryQueryParams(PyBaseModel):
    name: Optional[str] = None
    limit: Optional[int] = 100
    sort_by: Optional[List[SortProductCategoryBy]] = None
    skip: Optional[int] = 0
    order: Optional[SortOrder] = SortOrder.asc



# class IProductCategoryRefUpdate(PyBaseModel):
#     category_id: int
#     product_id: int
