#!/usr/bin/python3
"""lists all cities by state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # connection
    cnx = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          psswd=sys.argv[2], db=sys.argv[3])

    # cursor object creation
    c = cnx.cursor()

    # execution of SQL query script
    c.execute("SELECT cities.id, cities.name, states.name
              FROM cities, states
              WHERE cities.state_id=states.id
              ORDER BY cities.id ASC")

    # fetch remaining rows after script executed
    query_rows = c.fetchall()

    # printing query
    for row in query_rows:
        print(row)

    # close cursor and connection
    c.close()
    cnx.close()
