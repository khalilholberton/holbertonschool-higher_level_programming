#!/usr/bin/python3
# script that changes the name of a State object

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    mychange = session.query(State).filter(State.id == 2)
    mychange.update({"name": ("New Mexico")})
    session.commit()
    session.close()
