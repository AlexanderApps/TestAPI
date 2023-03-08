from datetime import date
from helper.sort_order_mapper import mapper
from models.product import Product
from schemas.iproduct import IProduct, IProductQueryParams
from helper.product_pretty import ProductValidator


class ProductActions:

    @staticmethod
    def create_product(product: IProduct, current_user: int):
        product_ = product.dict().copy()
        product_["last_updatedby"] = product_["createdby"] = current_user
        try:
            q: int = Product.insert(**product_).execute()
        except Exception as e:
            print(e)
            raise (e)
        return ProductActions.get_product_by_id(q)

    @staticmethod
    def get_products(params: IProductQueryParams):
        sb = mapper(Product, params.sort_by, params.order)
        sort_by = sb if sb else [Product.product_id]
        rows = (
            Product.select().where
            (
                (Product.name.contains(params.name)
                 if params.name else True) &
                (Product.expiry_date <= date.today()
                 if params.expired else True)
            )
            .order_by(*sort_by)
            .limit(params.limit)
            .offset(params.skip)
            .dicts()
        )
        print(rows.sql())
        return [row for row in rows]

    @staticmethod
    def get_product_by_id(id_: int):
        rows = Product.select().where(Product.product_id == id_).dicts()
        product = [row for row in rows]
        if len(product) == 1:
            return product[0]
        raise ValueError("Product not found")

    @staticmethod
    def get_product_by_name(name: str):
        rows = Product.select().where(Product.name == name).dicts()
        return [row for row in rows]

    @staticmethod
    def delete_product(id_: int, current_user: int):
        product = ProductActions.get_product_by_id(id_)
        Product.delete().where(Product.product_id == id_).execute()
        return product

    @staticmethod
    def update_product(id_: int, current_user: int):
        product = ProductActions.get_product_by_id(id_)
        Product.delete().where(Product.product_id == id_)
        return product

    @staticmethod
    def increase_quantity(id_: int, quantity: int):
        pass

    @staticmethod
    def decrease_quantity(id_: int, quantity: int):
        pass

    @staticmethod
    def update_quantity(id_: int, quantity: int):
        pass
