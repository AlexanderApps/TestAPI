from pydantic import BaseModel as PyBaseModel, EmailStr


class IUserDetail(PyBaseModel):
    user_phone: str | None = None
    user_address: str | None = None
    user_parent_name: str | None = None
    bank_account_name: str | None = None
    bank_account_number: str | None = None
    bank_name: str | None = None
    bank_branch: str | None = None
    next_of_kin_name: str | None = None
    next_of_kin_email: EmailStr | None = None
    next_of_kin_number: str | None = None
    next_of_kin_address: str | None = None
