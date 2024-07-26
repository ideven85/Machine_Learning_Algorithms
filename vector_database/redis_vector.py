import redis
r = redis.Redis(host="localhost", port=6379)

# res = r.set("bike", "Process 134")
# print(res)
# # >>> True
#
# res = r.get("bike")
# print(res)
# # >>> "Process 134"

bike =  r.hset(
    "deven_bike",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)

print(r.hget("deven_bike","model"))
print(r.hgetall("deven_bike"))

"""
Code samples for Hash doc pages:
    https://redis.io/docs/latest/develop/data-types/hashes/
"""
import redis

#r = redis.Redis(decode_responses=True)
res1 = r.hset(
    "bike",
    mapping={
        "model": "Deimos",
        "brand": "Ergonom",
        "type": "Enduro bikes",
        "price": 4972,
    },
)
# print(res1)
# # >>> 4

res2 = r.hget("bike", "model")
print(res2)
# >>> 'Deimos'

res3 = r.hget("bike", "price")
print(res3)
# >>> '4972'

res4 = r.hgetall("bike")
print(res4)
# >>> {'model': 'Deimos', 'brand': 'Ergonom', 'type': 'Enduro bikes', 'price': '4972'}


#
# res5 = r.hmget("bike", ["model", "price"])
# print(res5)
# # >>> ['Deimos', '4972']


res6 = r.hincrby("bike", "price", 100)
print(res6)
# >>> 5072
res7 = r.hincrby("bike", "price", -100)
print(res7)
# >>> 4972



res11 = r.hincrby("bike:stats", "rides", 1)
print(res11)
# >>> 1
res12 = r.hincrby("bike:stats", "rides", 1)
print(res12)
# >>> 2
res13 = r.hincrby("bike:stats", "rides", 1)
print(res13)
# >>> 3
res14 = r.hincrby("bike:stats", "crashes", 1)
print(res14)
# >>> 1
res15 = r.hincrby("bike:stats", "owners", 1)
print(res15)
# >>> 1
res16 = r.hget("bike:stats", "rides")
print(res16)
# >>> 3
res17 = r.hmget("bike:stats", ["crashes", "owners"])
print(res17)
# >>> ['1', '1']

