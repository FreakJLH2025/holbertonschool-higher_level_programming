#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password, database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute query: list all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
