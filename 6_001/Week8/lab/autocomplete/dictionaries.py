table = dict()
class A:
    def __init__(self):
        self=[32,33]
a=A()
vals = ({'A':1},{'B':2},{'A':3})
i=0
for val in vals:
    for key,value in val.items():
        table.setdefault(key,A()).append(a[i])
    i+=1


print(table)