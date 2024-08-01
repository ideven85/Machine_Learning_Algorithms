import psycopg2
import numpy as np

# Connect to PostgreSQL
conn = psycopg2.connect("dbname=lms user=deven password=728000")

# Create a cursor
cur = conn.cursor()

# Use pgvector extension (if not already created)
cur.execute("CREATE EXTENSION IF NOT EXISTS vector")

# Insert a vector into a table
vector = np.array([0.1, 0.2, 0.3])
cur.execute("INSERT INTO foo1 (vector_column) VALUES (%s)", (vector.tolist(),))

# Commit the transaction
conn.commit()

# Fetch and print the vectors
cur.execute("SELECT * FROM foo1")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()