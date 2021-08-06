#!/usr/bin/python3
"""
Lists all states matching the name argument from the database
`hbtn_0e_0_usa`.

"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    db.query("""SELECT * FROM states ORDER BY states.id ASC;""")
    rows = db.store_result()
    for row in rows.fetch_row(0):
        if row[1] == state_name:
            print(row)
