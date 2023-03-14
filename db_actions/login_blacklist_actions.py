from auth.oauth2 import ITokenData
from models.login_blacklist import LoginBlacklist


class LoginBlacklistActions:
    @staticmethod
    def blacklist_token(token_data: ITokenData):
        dt = LoginBlacklist.create(
            token=token_data.token,
            expiry=token_data.exp
        )
        return LoginBlacklist.get(dt)
