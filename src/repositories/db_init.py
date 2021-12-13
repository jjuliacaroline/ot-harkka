"""Modules"""
from repositories.database_connection import get_database_connection
conn = get_database_connection()



class Actions:

    def create_table():
        """Creates a table into the database"""
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS news (id INTEGER, text TEXT)''')
        conn.commit()

    def drop_table():
        """Deletes the table"""
        cur = conn.cursor()
        cur.execute('''DROP TABLE news''')
        conn.commit()

    def get_all_from_table():
        """Return all table elements"""
        cur = conn.cursor()
        cur.execute('''SELECT * FROM news''')
        data = cur.fetchall()
        conn.commit()
        return data

    def insert_to_table(id_str, text_str):
        """Insert values into the table"""
        cur = conn.cursor()
        cur.execute("INSERT INTO news (id, text) VALUES (?, ?)", (int(id_str), str(text_str)))
        conn.commit()

    def check_duplicates():
        """Checks for duplicates and returns a list of the duplicate values"""
        dup_lst = []
        cur = conn.cursor()
        cur.execute("SELECT text FROM news WHERE EXISTS(SELECT * FROM news)")
        duplicates = cur.fetchall()
        for i in duplicates:
            dup_lst.append(i)
        return dup_lst

    def row_count():
        """Returns floar value of the number of rows"""
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM news")
        count = float(cur.fetchone()[0])
        return count
