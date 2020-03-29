#!/usr/bin/python3
# script to lists all cities from database hbtn_0e_0_usa


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4], ))
    rows = c.fetchall()
    print(", ".join([row[0] for row in rows]))

    c.close()
    db.close()
