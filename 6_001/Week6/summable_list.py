class SumList(list):
    def sum(self):
        s = 0
        for v in self:
            s += v
        return s


def sum_right(seq):
    if not seq:
        return 0
    return seq[0] + sum_right(seq[1:])


def until(n, filter_func, v):
    if n == v:
        return 0

    if filter_func(v):
        return sum([v]) + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v + 1)


s = [1, 2, 3]
sum_list = SumList(s)
print(sum_list.sum())
print(sum_right(s))

print(until(10, lambda x: not x % 3 or not x % 5, 0))
print(sum([n for n in range(10) if not n % 3 or not n % 5]))
