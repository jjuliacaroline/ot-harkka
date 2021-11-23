from sqlite3.dbapi2 import Connection
from database_connection import get_database_connection

def create_table(connection):
    cur = connection.cursor()
    cur.execute('''CREATE TABLE news (id INTEGER, text TEXT''')

def initialize_db():
    conn = get_database_connection()
