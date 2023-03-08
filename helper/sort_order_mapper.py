from models.user import User
from typing import List, Optional, Union
from models.product import Product
from models.transaction import Transaction
from models.product_category import ProductCategory
from peewee import ModelBase
from schemas.iquery_params import SortOrder, SortProductBy, SortProductCategoryBy, SortTransactionBy, SortUserBy


def get_desc(mapper: dict) -> dict:
    return {x: y.desc() for x, y in mapper.items()}


map_orderby = (
    {
        "user": {
            "user_id": User.user_id,
            "user_name": User.user_name,
            "age": User.birthday,
            "access": User.access,
            "last_name": User.last_name,
            "first_name": User.first_name,
            "middle_name": User.middle_name,
        },

        "product": {
            "product_id": Product.product_id,
            "product_name": Product.name,
            "other_names": Product.other_names,
            "batch_number": Product.batch_number,
            "expiry_date": Product.expiry_date,
            "status": Product.status,
            "access": Product.access,
            "price": Product.price,
            "quantity": Product.quantity_available,
        },

        "transaction": {
            "transaction_id": Transaction.transaction_id,
            "transaction_name": Transaction.transaction_name,
            "access": Transaction.access,
            "date_created": Transaction.date_created,
            "status": Transaction.status,
            "createdby": Transaction.createdby,
            "last_updatedby": Transaction.last_updatedby,
            "amount": Transaction.amount,
        },

        "productcategory": {
            "category_id": ProductCategory.category_id,
            "category_name": ProductCategory.category_name,
            "description": ProductCategory.description,
        },

    }

)

OrderType = Union[
    None,
    List[SortUserBy],
    List[SortProductBy],
    List[SortTransactionBy],
    List[SortProductCategoryBy],
]


def mapper(model: ModelBase, sort_by: OrderType,
           order: Optional[SortOrder] = SortOrder.asc):
    if not sort_by:
        return
    name = model.__name__.lower()
    map_dict: dict = map_orderby.get(name, {})
    if order and order.value == "desc":
        dict_desc = get_desc(map_dict)
        return [dict_desc.get(x.value) for x in sort_by]
    return [map_dict.get(x.value) for x in sort_by]


# def map_user(sort_by: Optional[List[SortUserBy]] = None,
#              order: Optional[SortOrder] = SortOrder.asc):
#     if not sort_by:
#         return
#     if order and order.value == "desc":
#         user_sort_order_desc = get_desc(user_sort_order_mapper)
#         return [user_sort_order_desc.get(x.value) for x in sort_by]
#     return [user_sort_order_mapper.get(x.value) for x in sort_by]


# def map_product(sort_by: Optional[List[SortProductBy]] = None,
#                 order: Optional[SortOrder] = SortOrder.asc):
#     if not sort_by:
#         return
#     if order and order.value == "desc":
#         product_sort_order_desc = get_desc(product_sort_order_mapper)
#         return [product_sort_order_desc.get(x.value) for x in sort_by]
#     return [product_sort_order_mapper.get(x.value) for x in sort_by]


# def map_transaction(sort_by: Optional[List[SortTransactionBy]] = None,
#                     order: Optional[SortOrder] = SortOrder.asc):
#     if not sort_by:
#         return
#     if order and order.value == "desc":
#         transaction_sort_order_desc = get_desc(transaction_sort_order_mapper)
#         return [transaction_sort_order_desc.get(x.value) for x in sort_by]
#     return [transaction_sort_order_mapper.get(x.value) for x in sort_by]


# def map_product_category(sort_by: Optional[List[SortProductCategoryBy]] = None,
#                          order: Optional[SortOrder] = SortOrder.asc):
#     if not sort_by:
#         return
#     if order and order.value == "desc":
#         product_category_sort_order_desc = get_desc(
#             product_category_sort_order_mapper)
#         return [product_category_sort_order_desc.get(x.value) for x in sort_by]
#     return [product_category_sort_order_mapper.get(x.value) for x in sort_by]


# def map_order_by_func():
#     pass
