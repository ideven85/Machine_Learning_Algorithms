from datetime import datetime


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def transpose_normal(matrix):
    transposed = [[]]
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):
            if j < len(matrix) and i < len(matrix[j]):
                transposed[i].append(matrix[j][i])
        transposed.append([])
    return transposed[:-1]


def day_of_year(tm):
    return tm.timetuple().tm_yday


print(day_of_year(datetime(2024, 2, 29)))

a = list(range(1, 4))
b = list(range(2, 5))
m = [b, b, a]
print(m)
print(transpose(m))
print(transpose_normal(m))
print("\n".join((",".join(map(str, row)) for row in transpose(m))))
