#!/usr/bin/python3
# script that prints the first State object from the database hbtn_0e_6_usa


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).first()
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
    session.close()
