from enum import Enum


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class SortUserBy(str, Enum):
    user_id = "user_id"
    user_name = "user_name"
    age = "age"
    access = "access"
    last_name = "last_name"
    first_name = "first_name"
    middle_name = "middle_name"


class SortProductBy(str, Enum):
    product_id = "product_id"
    product_name = "product_name"
    access = "access"
    date_created = "date_created"
    price = "price"
    quantity = "quantity"
    created_by = "created_by"


class SortTransactionBy(str, Enum):
    transaction_id = "transaction_id"
    transaction_name = "transaction_name"
    access = "access"
    date_created = "date_created"
    status = "status"
    createdby = "createdby"
    amount = "amount",
    last_updatedby = "last_updatedby"


class SortProductCategoryBy(str, Enum):
    category_id = "category_id"
    category_name = "category_name"
    description = "description"
