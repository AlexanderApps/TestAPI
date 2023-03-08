from peewee import IntegerField, AutoField, ForeignKeyField, DecimalField

from models.product import Product
from models.transaction import Transaction
from models.base_model import BaseModel, database


class TransactionProduct(BaseModel):
    row_id = AutoField()
    transaction_id = ForeignKeyField(
        Transaction, backref="transactionproducts", index=True)
    product_id = ForeignKeyField(
        Product, backref="transactionproducts", index=True)
    quantity = IntegerField()
    price = DecimalField()


def create_transaction_product_table():
    with database:
        database.create_tables([TransactionProduct])


def drop_transaction_product_table():
    with database:
        database.drop_tables([TransactionProduct])
