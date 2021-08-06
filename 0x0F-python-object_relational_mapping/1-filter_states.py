#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database
`hbtn_0e_0_usa`.

"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to MySQL database based on command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Run the following query:
    query = """
            SELECT *
            FROM states
            WHERE name LIKE "N%"
            ORDER BY states.id ASC;
            """
    db.query(query)
    result = db.store_result()

    # Print the results
    for row in result.fetch_row(0):
            print(row)
