from models.user import create_user_table, drop_user_table
from models.state import create_status_table, drop_status_table
from models.access import create_access_table, drop_access_table
from models.product import create_product_table, drop_product_table
from models.transaction import create_transaction_table, drop_transaction_table
from models.user_detail import create_user_detail_table, drop_user_detail_table
from data_access.db_setup import init_access, init_admin, init_status, init_transaction_type
from models.product_category import create_product_category_table, drop_product_category_table
from models.transaction_type import create_transaction_type_table, drop_transaction_type_table
from models.transaction_product import create_transaction_product_table, drop_transaction_product_table
from models.product_category_ref import create_product_category_ref_table, drop_product_category_ref_table


create_tables_ = [
    create_access_table,
    create_status_table,
    create_user_table,
    create_product_table,
    create_user_detail_table,
    create_transaction_type_table,
    create_transaction_table,
    create_product_category_table,
    create_transaction_product_table,
    create_product_category_ref_table
]

drop_tables_ = [
    drop_product_category_ref_table,
    drop_user_detail_table,
    drop_transaction_product_table,
    drop_transaction_table,
    drop_product_table,
    drop_transaction_type_table,
    drop_product_category_table,
    drop_user_table,
    drop_status_table,
    drop_access_table,
]

init_tables_ = [
    init_access,
    init_transaction_type,
    init_status,
    init_admin,
]


def create_tables():
    for create_table in create_tables_:
        create_table()


def drop_tables():
    for drop_table in drop_tables_:
        drop_table()


def init_tables():
    for init_table in init_tables_:
        init_table()
