from models.user import User
from models.product import Product
from schemas.iproduct import IProduct
from models.transaction import Transaction
from helper.sort_order_mapper import mapper
from models.transaction_type import TransactionType
from schemas.itransaction_type import ITransactionType
from models.transaction_product import TransactionProduct
from db_actions.transaction_product_actions import TransactionProductActions
from schemas.itransaction import ITransaction, ITransactionBody, ITransactionItems, ITransactionQueryParams
from models.base_model import database


class TransactionActions:

    # @database.atomic()
    @staticmethod
    def create_transaction(transaction: ITransaction):
        try:
            is_valid = TransactionActions.__check_product_validity(transaction)
            transaction_dict = transaction.dict()
            if is_valid:
                TransactionActions.__execute_transaction(transaction)
                print(is_valid)
                items = transaction_dict["items"]
                print(items)
                del transaction_dict["items"]
                transaction_id = Transaction.insert(
                    **transaction_dict).execute()
                TransactionProductActions.create_transaction_product(
                    transaction_id, items)
                return transaction_dict
        except Exception as e:
            raise ValueError(e)

    @staticmethod
    def __check_product_validity(transaction: ITransaction):
        error_list = []
        transanction_type = transaction.type
        lookup_transac_type: ITransactionType = TransactionType.get(
            TransactionType.type_id == transanction_type)
        items = transaction.items
        if not len(items):
            raise ValueError("no product selected")
        for item in items:
            if lookup_transac_type.mod < 0:
                product: IProduct = Product.get(
                    Product.product_id == item.product_id)
                if not product.quantity_available >= item.quantity:
                    q_error = f"Product:{product.name}: Available: {product.quantity_available} Can't: {lookup_transac_type.type_name}- {item.quantity}"
                    error_list.append(q_error)
        if not (len(error_list)):
            return True
        error = "\n".join(error_list)
        # print(error)
        raise ValueError(f"{error}")

    @staticmethod
    def __execute_transaction(transaction: ITransaction):
        try:
            product_list = []
            transanction_type = transaction.type
            lookup_transac_type: ITransactionType = TransactionType.get(
                TransactionType.type_id == transanction_type)
            items = transaction.items
            if not len(items):
                raise ValueError("no product selected")
            for item in items:
                product: IProduct = Product.get(
                    Product.product_id == item.product_id)
                if lookup_transac_type.mod < 0:
                    product.quantity_available -= item.quantity
                    product_list.append(product)
                elif lookup_transac_type.mod > 0:
                    product.quantity_available += item.quantity
                    product_list.append(product)
                else:
                    return True
                Product.bulk_update(product_list, fields=[
                                    'quantity_available'])
            return True
        except Exception as e:
            raise ValueError(f"{e}")

    @staticmethod
    def get_transactions(params: ITransactionQueryParams):
        sb = mapper(Transaction, params.sort_by, params.order)
        sort_by = sb if sb else [Transaction.transaction_id]
        if params.name:
            rows = (
                Transaction.select()
                .where(
                    Transaction
                    .transaction_name
                    .contains(params.name)
                )
                .order_by(*sort_by)
                .limit(params.limit)
                .offset(params.skip)
                .dicts()
            )
        else:
            rows = (
                Transaction.select()
                .order_by(*sort_by)
                .limit(params.limit)
                .offset(params.skip)
                .dicts()
            )
        print(rows.sql())
        return [row for row in rows]

    @staticmethod
    def get_transaction_by_id(id_: int):
        rows = (
            Transaction
            .select()
            .where(Transaction.transaction_id == id_)
            .dicts()
        )
        val = [row for row in rows]
        if len(val) == 1:
            item_rows = TransactionProductActions.get_transaction_product_by_transaction_id(
                val[0]["transaction_id"])
            val[0]["items"] = [row for row in item_rows]
            return val[0]
        return {}

    @staticmethod
    def get_transaction_by_id2(id_: int):
        rows = (
            Transaction
            .select(
                Transaction.transaction_id,
                Transaction.transaction_name,
                Transaction.date_created,
                Transaction.last_updatedby,
                TransactionProduct.quantity,
                TransactionProduct.price,
                TransactionProduct.product_id,
                Transaction.type,
                TransactionType.type_name,
                Transaction.amount,
                Product.name,
                User.user_name
            )
            .join(TransactionProduct)
            .join(Product)
            .join(User, on=(Transaction.createdby == User.user_id))
            .join(TransactionType, on=(Transaction.type == TransactionType.type_id))
            .where(Transaction.transaction_id == id_)
            .dicts()
        )
        return TransactionActions.__parse_dict2(rows)

    @staticmethod
    def __parse_dict2(dict_d):
        val = [row for row in dict_d]
        items = [ITransactionItems(**row) for row in val]
        if len(val) >= 0:
            results = ITransactionBody(**val[0], items=items)
            return results
        raise ValueError("transaction is empty")

    @staticmethod
    def get_transaction_by_name(name: str):
        rows = Transaction.select().where(
            Transaction.transaction_name == name).dicts()
        return [row for row in rows]

    @staticmethod
    def get_transaction_by_name2(name: str):
        rows = Transaction.select().where(
            Transaction.transaction_name == name).dicts()
        rr = [row for row in rows]
        print(rr)
        if len(rr) == 1:
            _id = rr[0]["transaction_id"]
            tp_rows = TransactionProductActions.get_transaction_product_by_transaction_id(
                _id)
            rr[0]["items"] = tp_rows
        return rr[0]

    @staticmethod
    def get_transaction_by_name_filter(name: str):
        rows = (
            Transaction
            .select()
            .where(
                Transaction.transaction_name.contains(name)
            ).dicts()
        )
        return [row for row in rows]

    @staticmethod
    def delete_transaction(id_: int):
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
