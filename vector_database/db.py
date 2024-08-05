"""
Let’s represent the vector database using a 2D grid
 where one axis represents the color of the animal (brown, black, white)
 and the other axis represents the size (small, medium, large).
"""
import pandas as pd
import psycopg2
conn = psycopg2.connect("dbname=lms user=deven password=728000")
# db.run("CREATE TABLE foo (bar text, baz int)")
# db.run("INSERT INTO foo VALUES ('buz', 42)")
# db.run("INSERT INTO foo VALUES ('bit', 537)")

curr = conn.cursor()
curr.execute("CREATE TABLE foo (bar text, baz int)")
curr.execute("INSERT INTO foo VALUES ('buz', 42)")
conn.commit()

curr.close()
conn.close()
