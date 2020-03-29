#!/usr/bin/python3
# Python script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = my_cursor.fetchall()
    for row in rows:
        print(row)

        my_cursor.close()
    db.close()
