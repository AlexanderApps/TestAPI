from typing import List
from pydantic import BaseModel as PyBaseModel, validator

from schemas.iquery_params import SortOrder, SortProductCategoryBy


class IProductCategory(PyBaseModel):
    category_name: str
    description: str | None

    @validator("category_name")
    @classmethod
    def validate_category_name(cls, value):
        if value:
            value = value.strip().upper()
            value = " ".join(v for v in value.split(" ") if v != "")
            return value
        return value


class IProductCategoryUpdate(IProductCategory):
    category_name: str | None


class IProductCategoryRef(PyBaseModel):
    category_id: int
    product_id: int


class IProductCategoryRefAdd(PyBaseModel):
    product_id: int


class IProductCategoryQueryParams(PyBaseModel):
    name: str | None
    limit: int | None = 100
    sort_by: List[SortProductCategoryBy] | None
    skip: int | None = 0
    order: SortOrder | None = SortOrder.asc


# class IProductCategoryRefUpdate(PyBaseModel):
#     category_id: int
#     product_id: int
