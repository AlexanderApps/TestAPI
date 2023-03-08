from datetime import datetime
from pydantic import BaseModel as PyBasemodel


class ITransactionType(PyBasemodel):
    type_id: int
    type_name: str
    description: str | None = None
    mod: int
    date_created: datetime
