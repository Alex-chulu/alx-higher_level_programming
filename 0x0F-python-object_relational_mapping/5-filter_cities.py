#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


def filter_city():
    """Make a database connection
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
                ON cities.state_id=states.id \
                WHERE states.name=%s ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()

    list_data = []
    for row in query_rows:
        list_data.append(row[0])

    print(', '.join(list_data))

    db.close()


if __name__ == '__main__':
    filter_city()
