#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
Arguments: mysql username, mysql password, database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
