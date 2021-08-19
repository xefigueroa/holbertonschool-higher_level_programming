#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""

import MySQLdb
import sys


if __name__ == "__main__":
    # connection
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          psswd=sys.argv[2], db=sys.argv[3])

    # cursor object creation
    c = conn.cursor()

    # execution of SQL query script
    c.execute("SELECT * FROM states\
              WHERE name='{}'\
              ORDER BY states.id".format(argv[4]))

    # fetch remaining rows after script executed
    query_rows = c.fetchall()

    # printing query
    for row in query_rows:
        print(row)

    # close cursor and connection
    c.close()
    conn.close()
