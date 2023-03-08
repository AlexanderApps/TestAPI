from pydantic import BaseModel as PyBaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from models.user import User
from auth.oauth import verify_hash
from auth.oauth2 import ITokenData, create_access_token


class ILoginDetails(PyBaseModel):
    username: str
    password: str


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login")
async def login(seeker: OAuth2PasswordRequestForm = Depends()):
    try:
        user = User.get_or_none(User.user_name == seeker.username)
        valid = verify_hash(user.password, seeker.password)
        if not valid:
            raise ValueError("Invalid Credentials")
        token = create_access_token(ITokenData(
            user_id=user.user_id,
            access=user.access.row_id
        ))
        print(token)
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except Exception as e:
        print(e)
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail={
            "message": "Invalid Credentials"
        })
