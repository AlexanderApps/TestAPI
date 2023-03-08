from typing import Optional
from pydantic import BaseModel as PyBaseModel, EmailStr


class IUserDetail(PyBaseModel):
    user_phone: Optional[str] = None
    user_address: Optional[str] = None
    user_parent_name: Optional[str] = None
    bank_account_name: Optional[str] = None
    bank_account_number: Optional[str] = None
    bank_name: Optional[str] = None
    bank_branch: Optional[str] = None
    next_of_kin_name: Optional[str] = None
    next_of_kin_email: Optional[EmailStr] = None
    next_of_kin_number: Optional[str] = None
    next_of_kin_address: Optional[str] = None
