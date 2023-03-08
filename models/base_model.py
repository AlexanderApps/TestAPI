from peewee import Model

from data_access.connection_handler import database_connection

try:
    database = database_connection()
    if database: database.connect()
except Exception as e:
    print("Could not connect to database")
    print(e)
    exit()
if not database:
    print("Database connection was unsuccessful")
    exit()


class BaseModel(Model):
    class Meta:
        database = database

