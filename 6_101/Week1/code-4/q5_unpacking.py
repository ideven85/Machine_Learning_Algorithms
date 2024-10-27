#################### multiple assignment

# how can we swap two variables *without* using a variable like 'temp'?

a = 7
b = 8

b += a
a = b - a
b = b - a


assert a == 8 and b == 7


##################### unpacking (and star operator)

x = (9, 8, 7, 6, 5)

y, z = x[0], x[1:]

assert y == 9 and z == (8, 7, 6, 5)

print("all done")
