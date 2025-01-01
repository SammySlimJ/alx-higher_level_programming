#!/usr/bin/python3
"""
Displays al values in the states table of the database hbtn_0e_0_usa whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database nawe> \
                                <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
