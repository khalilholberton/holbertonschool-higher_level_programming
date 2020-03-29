#!/usr/bin/python3
# script that lists all State objects from the database hbtn_0e_6_usa


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()
    for instance in query:
        print("{}: {}".format(instance.id, instance.name))
