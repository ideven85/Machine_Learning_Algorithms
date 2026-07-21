# by the end of doing these exercises, we should be able
# to start to understand something like this:

## WAT >:O

o = ["cold", "cord", "word", "ward", "warm"]
x = all(
    (len(a) == len(b) and sum(i != j for i, j in zip(a, b)) == 1)
    for a, b in zip(o, o[1:])
)
print(x)
