import csv
import aiofiles
import asyncio
import datetime
import time

import yaml

from models.base_model import BaseModel
from models.product import Product
from models.transaction import Transaction
from models.transaction_product import TransactionProduct
from models.user import User
from pydantic import BaseModel as PyBaseModel
from db_actions.product_actions import ProductActions
from schemas.iproduct import IProduct
from db_actions.product_category_actions import ProductCategoryActions

# # async def get_data():
# #     async with aiofiles.open("data/dd.csv", "r") as f:
# #         data = await f.read()
# #         val = csv.DictReader(data)
# #         return val
    
# # d = asyncio.run(get_data())
# # for x in d:
# #     print(len(x))

# # def user_convert(val):
# #     val["access"] = int(val["access"])
# #     if val["status"] == "True":
# #         val["status"] = True
# #     else:
# #         val["status"] = False
# #     val["date_created"] = time.mktime(datetime.datetime.strptime(val["date_created"], "%Y-%m-%d %H:%M:%S").timetuple())
# #     val["last_updated"] = time.mktime(datetime.datetime.strptime(val["last_updated"], "%Y-%m-%d %H:%M:%S").timetuple())
# #     val["createdby"] = 1
# #     return val

# # def trans_pro_convert(val):
# #     val["transaction_id"] = int(val["transaction_id"])
# #     val["product_id"] = int(val["product_id"])
# #     val["price"] = float(val["price"])
# #     return val

# def transaction_convert(val):
#     val["access"] = int(val["access"])
#     val["status"] = int(val["status"])
#     val["createdby"] = int(val["createdby"])
#     val["date_created"] = int(val["date_created"])
#     val["last_updatedby"] = int(val["last_updatedby"])
#     val["last_updated"] = int(val["last_updated"])
#     val["amount"] = float(val["amount"])
#     return val


# def product_convert(val):
#     val["access"] = int(val["access"])
#     val["quantity_available"] = int(val["quantity_available"])
#     val["createdby"] = int(val["createdby"])
#     val["date_created"] = int(val["date_created"])
#     val["last_updatedby"] = int(val["last_updatedby"])
#     val["last_updated"] = int(val["last_updated"])
#     val["price"] = float(val["price"])
#     return val

# # with open("data/pp.csv", "r") as f:
# #     data = csv.DictReader(f)
# #     rows = map(product_convert, data)
# #     rows = [row for row in rows]
# #     print(rows)
# #     q = Product.insert_many(rows)
# #     # print(q.sql())
# #     q.execute()
# #     # for val in data:
# #     #     User.create()
# #         # print(**val)

# # with open("data/tt.csv", "r") as f:
# #     data = csv.DictReader(f)
# #     rows = map(transaction_convert, data)
# #     rows = [row for row in rows]
# #     print(rows)
# #     q = Transaction.insert_many(rows)
# #     # print(q.sql())
# #     q.execute()
#     # for val in data:
#     #     User.create()
#         # print(**val)


# # with open("data/dd.csv", "r") as f:
# #     data = csv.DictReader(f)
# #     rows = map(user_convert, data)
# #     rows = [row for row in rows]
# #     q = User.insert_many(rows)
# #     print(q.sql())
#     # q.execute()
#     # for val in data:
#     #     User.create()
#         # print(**val)


# # product = Product.get(Product.createdby == 1)
# # print(product)

# # transaction = Transaction.get(Transaction.access == 1)
# # print(transaction)

class IDummyProduct(PyBaseModel):
    name: str
    other_names: str
    batch_number: str
    expiry_date: datetime.date
    status: int
    access: int
    price: float
    quantity_available:int

def dummy_product():
    with open("data/dummy_product.csv", "r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            h = IDummyProduct(**row)
            ProductActions.create_product(h, 1)
            print(h)

dummy_product()
time.sleep(1)


class IDummyProductCategory(PyBaseModel):
    category_name: str
    description: str

def dummy_product_category():
    with open("data/dummy_category.csv", "r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            h = IDummyProductCategory(**row)
            ProductCategoryActions.create_category(h, 1)
            print(h)

dummy_product_category()
time.sleep(1)

class IDummyProductCategoryRef(PyBaseModel):
    category_id: int
    product_id: int

class dummy_cat_prod_ref():
    with open("data/dummy_cat_prod_ref.csv", "r") as f:
        rows = csv.DictReader(f)
        for row in rows:
            h = IDummyProductCategoryRef(**row)
            ProductCategoryActions.add_prod_category(h, 1)
            print(h)



dummy_cat_prod_ref()
time.sleep(1)
