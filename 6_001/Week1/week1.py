a=[301, 302, 303]
b=[a,a,a]


b[0][0]=342
print(a)
print(b)

print(id(a))
print(id(b))