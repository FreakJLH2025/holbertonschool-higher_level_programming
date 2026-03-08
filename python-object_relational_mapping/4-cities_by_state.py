#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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

    cursor = db.cursor()

    # Single execute() call: join cities with states
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
