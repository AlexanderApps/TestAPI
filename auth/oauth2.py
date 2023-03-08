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


class ITokenMaker(PyBaseModel):
    user_id: int
    access: int


class IEncode(PyBaseModel):
    user_id: int
    access: int
    exp: datetime


def create_access_token(data: ITokenData) -> str:
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
        id_: int = decoded_info.user_id
        access: int = decoded_info.access
        if not id_:
            raise credential_exception
        return ITokenData(user_id=id_, access=access)
    except JWTError:
        raise credential_exception


def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate token",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return verify_access_token(token, credential_exception)
