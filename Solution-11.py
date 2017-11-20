import sqlite3
from sqlite3 import Error

# Choosing python sqlite database to select everything from employee database.
# This is just a pseudo-code example

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by the db_file
    :parameters -> db_file: database file
    :returns Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_all_tasks(conn):
    """
    Query all rows in the employee table
    :parameters -> conn: the Connection object
    :returns:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM EMPLOYEE")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "C:\\sqlite\db\employee.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("Query Employee table")
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()
