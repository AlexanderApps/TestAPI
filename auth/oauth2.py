from jose import JWTError, jwt
from datetime import timedelta, datetime
from pydantic import BaseModel as PyBaseModel
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from data_access.load_env import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRATION_TIME

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class IToken(PyBaseModel):
    username: str
    password: str


class ITokenData(PyBaseModel):
    user_id: int
    access: int
    exp: datetime
    token: str


class ITokenMaker(PyBaseModel):
    user_id: int
    access: int


class IEncode(PyBaseModel):
    user_id: int
    access: int
    exp: datetime


class ILogoutData(PyBaseModel):
    token: str
    exp: datetime


def create_access_token(data: ITokenMaker) -> str:
    to_encode = data.dict()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
    to_encode.update({"exp": expire})
    encode_val = IEncode(**to_encode)
    encoded_jwt = jwt.encode(
        encode_val.dict(), SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        decoded_info = IEncode(**payload)
        if not decoded_info.user_id:
            raise credential_exception
        return ITokenData(token=token, **decoded_info.dict())
    except JWTError:
        raise credential_exception
    except Exception as e:
        print(e)
        raise credential_exception


def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate token",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return verify_access_token(token, credential_exception)
