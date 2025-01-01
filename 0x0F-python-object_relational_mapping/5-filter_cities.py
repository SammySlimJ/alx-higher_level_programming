#!/usr/bin/python3
"""
THis script lists all cities of a given state from the database, hbtn_0e_4_usa, 
Safe from SQL Injection.
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name>
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

    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
