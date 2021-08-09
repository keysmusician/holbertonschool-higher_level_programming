#!/usr/bin/python3
"""Add the State object “Louisiana” to the database `hbtn_0e_6_usa`."""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state_name = "Louisiana"
    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()
    print(new_state.id)
