from pydantic import BaseModel as PyBaseModel


class IProductTransaction(PyBaseModel):
    product_id: int
    quantity: int
    price: float
