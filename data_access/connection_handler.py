import yaml
from enum import Enum
from peewee import MySQLDatabase, SqliteDatabase, PostgresqlDatabase
from data_access.load_env import SQLITE_CONNECTION, \
    POSTGRES_CONNECTION, MYSQL_CONNECTION, ACTIVE_CONNECTION


def mysql_db():
    return MySQLDatabase("people", **MYSQL_CONNECTION)


def sqlite3_db():
    return SqliteDatabase(SQLITE_CONNECTION)


def postgres_db():
    return PostgresqlDatabase("people", **POSTGRES_CONNECTION)


class DBOptions(str, Enum):
    mysql = "mysql"
    sqlite = "sqlite"
    postgres = "postgres"


def database_connection():
    active_db: DBOptions = ACTIVE_CONNECTION
    try:
        db_opt = DBOptions(active_db)
    except ValueError as e:
        raise ValueError(
            f"{e}\n`{active_db}` could not be resolved.\nOptions are sqlite|mysql|postgres")
    print(f"Current active database is {active_db}")
    if db_opt.value == "postgres":
        return postgres_db()
    if db_opt.value == "mysql":
        return mysql_db()
    if db_opt.value == "sqlite":
        return sqlite3_db()
    raise ValueError("Could not properly connect to database")
