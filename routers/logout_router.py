from fastapi import APIRouter, Depends

from auth.oauth2 import ITokenData, get_current_user
from db_actions.login_blacklist_actions import LoginBlacklistActions


router = APIRouter(
    tags=["Logout"]
)

@router.post("/logout")
async def logout(current_user: ITokenData = Depends(get_current_user)):
    LoginBlacklistActions.blacklist_token(current_user)