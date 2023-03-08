
from typing import List
from models.transaction import Transaction
from models.transaction_product import TransactionProduct


class TransactionProductActions:
    @staticmethod
    def create_transaction_product(
        transaction_id: int,
        transaction_products: List[TransactionProduct]
    ):
        rows = TransactionProductActions.__add_tId(
            transaction_id, transaction_products)
        TransactionProduct.insert_many(rows).execute()
        return

    @staticmethod
    def get_transaction_products():
        return [row for row in Transaction.select().dicts()]

    @staticmethod
    def get_transaction_product_by_transaction_id(id_: int):
        rows = TransactionProduct.select().where(
            TransactionProduct.transaction_id == id_).dicts()
        return [row for row in rows]

    @staticmethod
    def delete_transaction_product(id_: int):
        pass

    @staticmethod
    def increase_quantity(id_: int, quantity: int):
        pass

    @staticmethod
    def decrease_quantity(id_: int, quantity: int):
        pass

    @staticmethod
    def update_quantity(id_: int, quantity: int):
        pass

    @staticmethod
    def __add_tId(tid: int, tp: List[TransactionProduct]):
        def add_tid(val):
            val["transaction_id"] = tid
            return val
        rows = map(add_tid, tp)
        return [row for row in rows]
