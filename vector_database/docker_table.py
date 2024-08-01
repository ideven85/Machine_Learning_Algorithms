import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="test",
    user="postgres",
    password="secret",
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Ensure the pgvector extension is enabled
cur.execute("CREATE EXTENSION IF NOT EXISTS vector")

# Create a table with a vector column
cur.execute("""
CREATE TABLE IF NOT EXISTS your_table (
    id SERIAL PRIMARY KEY,
    vector_column VECTOR(3)
)
""")

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Table created successfully")