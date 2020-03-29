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
    c.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
