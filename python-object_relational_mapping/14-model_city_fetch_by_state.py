#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
Arguments: mysql username, mysql password, database name
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query all cities joined with states, ordered by city id
    results = session.query(City, State).join(State).order_by(City.id).all()

    # Display results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
