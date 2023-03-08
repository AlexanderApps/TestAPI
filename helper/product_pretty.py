from typing import Union

from schemas.iproduct import IProduct, IProductUpdate
from schemas.iproduct_category import IProductCategory, IProductCategoryUpdate


class ProductValidator:

    @staticmethod
    def product_validate(product: Union[IProduct, IProductUpdate]):
        if product.name:
            product.name = product.name.upper()
        return product

    @staticmethod
    def category_validate(category: Union[IProductCategory, IProductCategoryUpdate]):
        if category.category_name:
            category.category_name = category.category_name.upper()
        return category
