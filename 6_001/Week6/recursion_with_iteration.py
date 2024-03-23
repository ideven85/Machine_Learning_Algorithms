import time
def original_sum_list(x):
    if not x:
        return 0
    return x[0]+ original_sum_list(x[1:])
def sum_list_iterative(x):
    sum_so_far=0
    for element in x:
        sum_so_far+=element
    return sum_so_far
count = 0
def sum_list(x):

    def sum_list_helper(sum_so_far,lst):

        if not lst:
            return sum_so_far

        first=lst[0]
        rest=lst[1:]
        return sum_list_helper(sum_so_far+first,rest)


    return sum_list_helper(0,x)
def sum_listV2(x,i=0,sum_so_far=0):
    if i>=len(x):
        return sum_so_far
    return sum_listV2(x,i+1,sum_so_far+x[i])
def sum_nested(original_x):
    sum_so_far=0
    agenda = [original_x]

    while agenda:
        x = agenda.pop(-1)
        if not x:
            sum_so_far += 0
        elif isinstance(x[0],list):
            agenda.append(x[0])
            agenda.append(x[1:])
        else:
            sum_so_far +=x[0]
            agenda.append(x[1:])
    return sum_so_far
def sum_nested_recursive(original_x):
    if not original_x:
        return 0
    elif isinstance(original_x[0],list):
        return sum_nested_recursive(original_x[0])+sum_nested_recursive(original_x[1:])
    else:
        return original_x[0]+sum_nested_recursive(original_x[1:])
if __name__ == '__main__':
    l = list(range(1,102))

    print("Sum List V2")
    start = time.time()
    print(sum_listV2(l))
    end = time.time()
    print((end - start)*1000000)
    print("Sum List Iterative")

    start = time.time()
    print(sum_list_iterative(l))
    end = time.time()
    print((end - start) * 1000000)

    print("Sum List Helper")
    start = time.time()
    print(sum_list(l))
    end = time.time()
    print((end - start) * 1000000)

    print("Original Sum List")
    start = time.time()
    print(original_sum_list(l))
    end = time.time()
    print((end - start)*1000000)

    a = [1,[2,3],[[list(range(4,100))]],101]

    print("Iterative Nested Sum List")
    start = time.time()
    print(sum_nested(a))
    end = time.time()
    print((end - start)*1000000)

    print("Recursive Nested Sum List")


    start = time.time()
    print(sum_nested_recursive(a))
    end = time.time()
    print((end - start) * 1000000)
