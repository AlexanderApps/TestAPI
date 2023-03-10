import yaml

with open("config.yaml", "r") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)


MYSQL_CONNECTION = cfg["database"]["mysql"]
ACTIVE_CONNECTION = cfg["database"]["active"]
POSTGRES_CONNECTION = cfg["database"]["postgres"]
SQLITE_CONNECTION = cfg["database"]["sqlite"]["db_name"]

ALGORITHM = cfg["auth"]["algorithm"]
SECRET_KEY = cfg["auth"]["secret_key"]
ACCESS_TOKEN_EXPIRATION_TIME = cfg["auth"]["access_token_expiration_time"]


print(MYSQL_CONNECTION)
print(SQLITE_CONNECTION)
print(POSTGRES_CONNECTION)
print(ACTIVE_CONNECTION)


print(ALGORITHM)
print(SECRET_KEY)
print(ACCESS_TOKEN_EXPIRATION_TIME)
