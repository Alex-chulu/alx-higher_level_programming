#!/usr/bin/python3
"""a script that takes in arguments and displays all values in 
the states table of hbtn_0e_0_usa"""

import MySQLdb
import sys


def filteriny():
    """Make a database connection """
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4],))
    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)

    db.close()

if __name__ == '__main__':
    filteriny()
