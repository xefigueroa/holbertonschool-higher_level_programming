#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""

import MySQLdb
import sys


if __name__ == "__main__":
    # connection
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    # cursor object creation
    cur = conn.cursor()

    # execution of SQL query script
    cur.execute("SELECT * FROM states \
              WHERE name LIKE BINARY '{}' \
              ORDER BY states.id ASC".format(argv[4]))

    # fetch remaining rows after script executed
    query_rows = cur.fetchall()

    # printing query
    for row in query_rows:
        print(row)

    # close cursor and connection
    cur.close()
    conn.close()
