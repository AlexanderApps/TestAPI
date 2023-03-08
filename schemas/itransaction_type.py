from datetime import datetime
from typing import Optional
from pydantic import BaseModel as PyBasemodel


class ITransactionType(PyBasemodel):
    type_id: int
    type_name: str
    description: Optional[str] = None
    mod: int
    date_created: datetime
