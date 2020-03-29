#!/usr/bin/python3
# displays all values in the states table of hbtn_0e_0_usa

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()

    for row in rows:
        if row[1] == argv[4]:
            print(row)

    c.close()
    db.close()
