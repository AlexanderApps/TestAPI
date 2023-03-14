from auth.oauth2 import ITokenData
from models.login_refresh_token import LoginRefreshToken


class LoginRefreshTokenActions:
    @staticmethod
    def blacklist_token(token_data: ITokenData):
        dt = LoginRefreshToken.create(
            token=token_data.token,
            expiry=token_data.exp
        )
        return LoginRefreshToken.get(dt)
