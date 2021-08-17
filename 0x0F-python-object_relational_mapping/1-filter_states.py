#!/usr/bin/python3
"""Module lists all states with a name starting with N"""
import MySQLdb
import sys


if __name__ == "__main__":
    """We are documenting this here to see if passes"""
    cnx = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          psswd=sys.argv[2], db=sys.argv[3])
    c = cnx.cursor()
    c.execute("SELECT * FROM states
              WHERE name LIKE 'N%'
              ORDER BY states.id ASC")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    cnx.close()
