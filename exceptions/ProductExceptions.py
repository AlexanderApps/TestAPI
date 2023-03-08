class ProductNotFound(Exception):
    def __init__(self, message: str) -> None:
        super().__init__("...")


raise ProductNotFound("Happy")