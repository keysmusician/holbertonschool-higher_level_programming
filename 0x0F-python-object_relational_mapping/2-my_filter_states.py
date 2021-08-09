#!/usr/bin/python3
"""
Lists all states matching the name argument from the database
`hbtn_0e_0_usa`.

"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to MySQL database based on command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Run the following query:
    query = """
            SELECT *
            FROM states
            WHERE name = '{}'
            ORDER BY states.id ASC;
            """.format(state_name)
    c = db.cursor()
    c.execute(query)
    record = c.fetchall()
    for row in record:
        if row[1][:1] == "N":
            print("({}, \'{}\')".format(row[0], row[1]))
    c.close()
    db.close()
