#!/usr/bin/python3
"""lists all cities by state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # connection
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    # cursor object creation
    cur = conn.cursor()

    # execution of SQL query script
    cur.execute("SELECT cities.id, cities.name, states.name \
              FROM cities JOIN states \
              WHERE cities.state_id = states.id \
              ORDER BY cities.id ASC")

    # fetch remaining rows after script executed
    query_rows = cur.fetchall()

    # printing query
    for row in query_rows:
        print(row)

    # close cursor and connection
    cur.close()
    conn.close()
