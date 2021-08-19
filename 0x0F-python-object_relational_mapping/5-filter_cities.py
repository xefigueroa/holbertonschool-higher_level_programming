#!/usr/bin/python3
"""Module takes name of a state as argument and lists all cities of state"""
import MySQLdb
import sys


if __name__ == "__main__":
    # connection
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           psswd=sys.argv[2], db=sys.argv[3])
    # cursor object creation
    c = conn.cursor()
    # execution of SQL query script
    c.execute("SELECT cities.name FROM cities\
              JOIN states ON cities.state_id=states.id\
              WHERE states.name=%s\
              ORDER BY cities.id", (sys.argv[4],))
    # fetch remaining rows after script executed
    query_rows = c.fetchall()
    # printing query
    print(", ".join(row[0] for row in query_rows))
    # close cursor and connection
    c.close()
    conn.close()
