from fastapi import APIRouter, Depends

from auth.oauth2 import ITokenData, get_current_user
from db_actions.login_refresh_token_actions import LoginRefreshTokenActions


router = APIRouter(
    tags=["Logout"]
)

@router.post("/logout")
async def logout(current_user: ITokenData = Depends(get_current_user)):
    LoginRefreshTokenActions.blacklist_token(current_user)