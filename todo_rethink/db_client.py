import os
from rethinkdb import r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

RDB_HOST = 'localhost'
RDB_PORT = 28015

PROJECT_DB = 'todo'
PROJECT_TABLE = 'notes'

db_connection = r.connect(RDB_HOST, RDB_PORT)

def dbsetup():
    try:
        r.db_create(PROJECT_DB).run(db_connection)
        print("Database setup completed")
    except RqlRuntimeError:
        try:
            r.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print("Table creation completed")
        except:
            print("Table already exists. Nothing to do")

dbsetup()
