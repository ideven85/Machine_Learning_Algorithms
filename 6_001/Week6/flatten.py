import time


def flatten(x):

    for elt in x:
        if isinstance(elt, list):
            yield from flatten(elt)
            # print(out)

        else:
            yield elt

# def sum_nested(x,total=0):
#     def sum_nested_helper(lst,i=0,sum_so_far=0):
#         if i>=len(lst):
#             return sum_so_far
#         else:
#             return sum_nested_helper(lst,i+1,lst[i]+sum_so_far)
#
#     if not x:
#         return total
#
#     if isinstance(x[0],list):
#         total+=sum_nested_helper(x[0])+sum_nested(x[1:])
#     else:
#         return sum_nested(x[1:],total+x[0])

# Tree Like Pattern
def sum_nested(x):
    sum_so_far=0
    if not x:
        return sum_so_far
    agenda = [x]
    while agenda:
        current = agenda.pop(-1)
        print(current)
        if not current:
            sum_so_far+=0
        elif isinstance(current[0],list):

            agenda.append(current[0])
            agenda.append(current[1:])
        else:
            print(current[1:])
            sum_so_far+=current[0]
            agenda.append(current[1:])
    return sum_so_far






x = [1]
y = [[[[[[[1, 2, 3]]]]], 4], 5]
print(sum_nested(x))
print(list(flatten(x)))
print(list(flatten(y)))
# print(flatten(y))


def flatten_list(x):
    out = []
    for el in x:
        if isinstance(el, list):
            out.extend(flatten_list(el))
        else:
            out.append(el)
    return out


def flatten_me(x):
    def is_flat(lst):
        for el in lst:
            if isinstance(el, list):
                return False
        return True

    if is_flat(x):
        return x
    else:

        out = []
        for el in x:
            if isinstance(el, list):
                f = flatten_me(el)
                for element in f:
                    out.append(element)
            else:
                out.append(el)
        return out


s1 = time.time_ns()
print(flatten_me(y))
s2 = time.time_ns()
print(flatten_list(y))
s3 = time.time_ns()
x1 = flatten(y)
while x1 is not None:
    a = x1
    if a.__iter__ < 2:
        raise StopIteration("asd")

    print(a.__next__(), end=" ")

s4 = time.time_ns()
print()
print("First", s2 - s1)
print("Second:", s3 - s2)
print("Generator:", s4 - s3)
