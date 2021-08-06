#!/usr/bin/python3
"""Lists all cities from the database `hbtn_0e_4_usa`."""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to a MySQL database based on command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Run the following query:
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON states.id = cities.state_id
            ORDER BY cities.id ASC;
            """
    cursor.execute(query)

    # Print the results
    for row in cursor.fetchall():
        print(row)
