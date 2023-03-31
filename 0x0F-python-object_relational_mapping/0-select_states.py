#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """Create a database connection """
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for row in cur.fetchall():
        print(row)

    db.close()
