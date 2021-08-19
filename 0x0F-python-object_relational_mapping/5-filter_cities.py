#!/usr/bin/python3
"""Module takes name of a state as argument and lists all cities of state"""
import MySQLdb
import sys


if __name__ == "__main__":
    # connection
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    # cursor object creation
    cur = conn.cursor()
    # execution of SQL query script
    cur.execute("SELECT cities.name FROM cities \
              JOIN states ON cities.state_id = states.id \
              WHERE states.name = %s \
              ORDER BY cities.id ASC", (sys.argv[4],))
    # fetch remaining rows after script executed
    query_rows = cur.fetchall()
    # printing query
    print(", ".join(row[0] for row in query_rows))
    # close cursor and connection
    cur.close()
    conn.close()
