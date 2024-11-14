import MySQLdb
import sqlite3

# Open database connection
db = MySQLdb.connect("localhost", "root", "root@123")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("DROP DATABASE TUTORIALS")

print("Database dropped")

# disconnect from server
db.close()
