from models.state import Status
from models.product import Product
from helper.sort_order_mapper import mapper
from models.product_category import ProductCategory
from models.product_category_ref import ProductCategoryRef
from schemas.iproduct_category import IProductCategory, IProductCategoryQueryParams, IProductCategoryRef, IProductCategoryUpdate


class ProductCategoryActions:

    @staticmethod
    def create_category(category: IProductCategory, current_user: int):
        category_ = category.dict().copy()
        category_["createdby"] = current_user
        try:
            q: int = ProductCategory.insert(**category_).execute()
            return ProductCategoryActions.get_category_by_id(q)
        except Exception as e:
            print(e)
            raise (e)

    @staticmethod
    def get_categories(params: IProductCategoryQueryParams):
        sb = mapper(ProductCategory, params.sort_by, params.order)
        sort_by = sb if sb else [ProductCategory.category_id]
        rows = (
            ProductCategory.select()
            .where(
                ProductCategory
                .category_name
                .contains(params.name)
                if params.name else True
            )
            .order_by(*sort_by)
            .limit(params.limit)
            .offset(params.skip)
            .dicts()
        )
        print(rows.sql())
        return [row for row in rows]

    @staticmethod
    def get_category_by_id(id_: int):
        rows = (
            ProductCategory.select().where(
                ProductCategory.category_id == id_
            ).dicts()
        )
        category = [row for row in rows]
        try:
            return category[0]
        except IndexError:
            raise ValueError("Category not found")

    @staticmethod
    def get_category_by_name(name: str):
        rows = ProductCategory.select().where(
            ProductCategory.category_name == name).dicts()
        return [row for row in rows]

    @staticmethod
    def delete_category(id_: int, current_user: int):
        category = ProductCategoryActions.get_category_by_id(id_)
        ProductCategory.delete().where(ProductCategory.category_id == id_).execute()
        return category

    @staticmethod

    def update_category(category_id: int, category: IProductCategoryUpdate, current_user: int):
        category_ = {x: y for x, y in category.dict().items()
                     if y != None}.copy()
        ProductCategory.update(
            **category_).where(ProductCategory.category_id == category_id).execute()
        return ProductCategoryActions.get_category_by_id(category_id)

    @staticmethod
    def get_category_items(category_id: int, current_user: int):
        # rows = ProductCategoryRef.select().where(ProductCategoryRef.category_id == category_id).dicts()
        __rows = (
            ProductCategoryRef.select(
                ProductCategory.category_id,
                ProductCategory.category_name,
                ProductCategoryRef.product_id,
                Product.name,
                Product.other_names,
                Product.batch_number,
                Product.price,
                Product.quantity_available,
                Product.status,
                Status.status_name
            ).join(ProductCategory)
            .join(Product, on=(ProductCategoryRef.product_id == Product.product_id))
            .join(Status, on=(Product.status == Status.row_id))
            .where(ProductCategoryRef.category_id == category_id)
            .dicts()
        )
        return [row for row in __rows]

    @staticmethod
    def add_prod_category(cat_prod_ref: IProductCategoryRef, current_user: int):
        rows = ProductCategoryRef.select().where(
            (ProductCategoryRef.product_id == cat_prod_ref.product_id) &
            (ProductCategoryRef.category_id == cat_prod_ref.category_id)
        )
        rows_ = [row for row in rows]
        if len(rows_):
            raise ValueError("product already in category")
        ProductCategoryRef.insert(**cat_prod_ref.dict()).execute()
        return {"add": (f"Prod: {cat_prod_ref.product_id} === Cat: {cat_prod_ref.category_id}")}

    @staticmethod
    def remove_prod_from_category(cat_prod_ref: IProductCategoryRef, current_user: int):
        rows = ProductCategoryRef.select().where(
            (ProductCategoryRef.product_id == cat_prod_ref.product_id) &
            (ProductCategoryRef.category_id == cat_prod_ref.category_id)
        )
        rows_ = [row for row in rows]
        if not len(rows_):
            raise ValueError("product not in category")
        rows[0].delete_instance()
        return {"removed": f"Prod: {cat_prod_ref.product_id} === Cat: {cat_prod_ref.category_id}"}
