#!/usr/bin/python3
"""
Lists all states matching the name argument from the database
`hbtn_0e_0_usa`. Safe from SQL injections.

"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to a MySQL database based on command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    # Run the following query:
    query = """
            SELECT *
            FROM states
            WHERE name = %s
            ORDER BY states.id ASC;
            """
    cursor.execute(query, (state_name,))

    # Print the results
    for row in cursor.fetchall():
        print(row)
