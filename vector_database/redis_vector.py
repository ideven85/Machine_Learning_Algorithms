import redis

# Connect to Redis
client = redis.Redis(host="localhost", port=6379, db=0)

# Ensure RediSearch module is loaded and create index
try:
    client.execute_command(
        "FT.CREATE",
        "myIndex1",
        "SCHEMA",
        "vector",
        "VECTOR",
        "HNSW",
        "6",
        "TYPE",
        "FLOAT32",
        "DIM",
        "3",
        "DISTANCE_METRIC",
        "COSINE",
    )
except redis.exceptions.ResponseError as e:
    print(f"Index creation error: {e}")

# Add a vector to the index
vector = [0.1, 0.2, 0.3]
client.hset("vec", {"vector": str(vector)})

# Search for the nearest vector
query = "KNN 1 @vector $vec PARAMS 2 vec [0.1,0.2,0.3] DIALECT 2"
result = client.execute_command("FT.SEARCH", "myIndex1", query)

print("Search result:", result)
