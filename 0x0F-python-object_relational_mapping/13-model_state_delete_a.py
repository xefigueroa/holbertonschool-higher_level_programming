#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Initialize engine
    Base.metadata.create_all(engine)

    # Initialize session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()

    # Close session
    session.close()
