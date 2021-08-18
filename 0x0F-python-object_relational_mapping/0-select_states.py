#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    cnx = MySQLdb.connect("localhost", 3306, sys.argv[1],
                          sys.argv[2], sys.argv[3])
    c = cnx.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    cnx.close()
