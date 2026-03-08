#!/usr/bin/python3
"""
Safe script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (protected from SQL injection).
Arguments: mysql username, mysql password, database name, state name searched
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
