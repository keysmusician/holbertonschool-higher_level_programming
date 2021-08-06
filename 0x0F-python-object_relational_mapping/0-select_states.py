#!/usr/bin/python3
"""Lists all states from the database `hbtn_0e_0_usa`."""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    db.query("""SELECT * FROM states ORDER BY states.id ASC;""")
    rows = db.store_result()
    for row in rows.fetch_row(0):
        print(row)
