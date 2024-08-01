import psycopg2
conn = psycopg2.connect("dbname=lms user=deven password=728000")

cur = conn.cursor()
cur.execute("SELECT * FROM foo")

rows = cur.fetchall()
for row in rows:
    print(row)