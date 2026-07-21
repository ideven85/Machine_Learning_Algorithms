import pickle
from collections import defaultdict

bacon_numbers = defaultdict(str)
# acted_together = list(tuple)


names = [[]]
with open("resources/names.pickle", "rb") as f:
    data = pickle.load(f)
    i = 0
    for key, value in data.items():
        bacon_numbers[value] = key
        if i == 2:
            continue
        print(key, value)
        i += 1


# for key,value in bacon_numbers.items():
#     print(key,value)
# print(bacon_numbers)
with open("resources/small.pickle", "rb") as f:
    data = pickle.load(f)
    print(data[1][2])
    for line in data:
        temp = []
        temp.append(bacon_numbers.get(line[0]))
        temp.append(bacon_numbers.get(line[1]))
        temp.append(bacon_numbers.get(line[2]))
        names.append(temp)

print(bacon_numbers.get("200015"))
a = (1, 2, 3)
print(a[0])
print(names)
# for line in data[:20]:
#     names.append(bacon_numbers[line[0]])
#     names.append(bacon_numbers[line[1]])
#     names.append(bacon_numbers[line[2]])
