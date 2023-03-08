from datetime import datetime
from peewee import AutoField, TimestampField, ForeignKeyField

from models.product import Product
from models.base_model import BaseModel, database
from models.product_category import ProductCategory


class ProductCategoryRef(BaseModel):
    row_id = AutoField(index=True)
    category_id = ForeignKeyField(ProductCategory, index=True)
    product_id = ForeignKeyField(Product, index=True)
    date_created = TimestampField(default=datetime.now)

    


def create_product_category_ref_table():
    with database:
        database.create_tables([ProductCategoryRef])


def drop_product_category_ref_table():
    with database:
        database.drop_tables([ProductCategoryRef])
