#!/usr/bin/python3
# script that prints the State object with the name passed as argument


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(State).filter(
            State.name == argv[4]).first()

    if item:
        print(item.id)
    else:
        print("Not found")

    session.close()
