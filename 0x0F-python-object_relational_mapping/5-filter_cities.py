#!/usr/bin/python3
"""Lists all cities of `state_name` in the database `hbtn_0e_4_usa`."""
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
            SELECT cities.name
            FROM cities
            WHERE state_id = (
                SELECT states.id
                FROM states
                WHERE states.name = %s
            )
            ORDER BY cities.id ASC;
            """
    cursor.execute(query, (state_name,))

    # Print the results
    result = ", ".join([row[0] for row in cursor.fetchall()])
    print(result)

    cursor.close()
