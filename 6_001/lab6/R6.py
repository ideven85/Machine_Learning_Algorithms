from collections import OrderedDict
from types import NoneType


def can_log(x):
    """"
    Checks whether the log entry is valid or not
    Valid entries are blah blah blah
    """
    if isinstance(x,(str,float,int,bool,NoneType,complex)):
        return True
    elif isinstance(x,(list,tuple,set,frozenset)):
        return all(can_log(v) for v in x)

    elif isinstance(x,(dict,OrderedDict)):
        return all((can_log(k)and can_log(v))  for k,v in x.items())
    else:
        return False

a = OrderedDict(a=1,b=2,c=3)
print(can_log(a))
for k in a.keys():
    print(k,end=' ')

def sum_list(x):
    """
    Compute the sum of list recursively
    >>> sum_list([1,2,3])
    6
    """
    if len(x)==0:
        return 0
    if len(x)==1:
        return x[0]
    return x[0]+sum_list(x[1:])
#todo Redo
def sum_nested(x):
    """
    Sums a nested list
    >>> sum_nested([[1,2],3,[4,5],[[[6]]]])
    21
    """
    if not x or len(x)==0:
        return 0
    if type(x[0]) is list:
       return sum_nested(x[0])+sum_nested(x[1:])
    else:
        return x[0]+sum_nested(x[1:])

def productSum(array,multiplier=1):
    # Write your code here.
    total = 0
    if not array:
        return 0

    elif type(array[0]) is list:
        return productSum(array[0],multiplier=multiplier+1)*multiplier+productSum(array[1:],multiplier=multiplier)
    else:
       return array[0]*multiplier +productSum(array[1:],multiplier=multiplier)

    # for e in array:
    #     if type(e) is list:
    #         total+=productSum(e,multiplier+1)
    #     else:
    #         total+=e
    # return total*multiplier

count=0
def subsequences(seq):

    """
    Given a tuple or list or other iterable, returns a set of tuples
    consisting of all its subsequences.
    A subsequence is a sequence of elements from seq that are in the same
    order as in seq but not necessarily adjacent.
    >>> sorted(subsequences([4,2,3]))
    [(), (2,), (2, 3), (3,), (4,), (4, 2), (4, 2, 3), (4, 3)]
    """
    global count
    if not seq:
        count+=1
        return {()}
    first= seq[0]
    rest = seq[1:]
    count+=1
    rest_seq = subsequences(rest)
    first_seq = {(first,)+sub_seq for sub_seq in rest_seq}
    return first_seq|rest_seq
    # answer= ({(first,) + subseq for subseq in subsequences(rest)} |
    #           {subseq for subseq in subsequences(rest)})
    # return answer



def powerset(array):

    c=0
    subSets = [[]]
    if not array:
        c+=1
        return {()}

    for element in array:
        for i in range(len(subSets)):
            c += 1
            currentSubSet = subSets[i]
            subSets.append(currentSubSet+ [element])
    print("Powerset Inversions: ", c)
    return subSets


def number_to_string(n, b):
    """
    Given an integer n and base b (where 2 <= b <= 10),
    returns n represented as a string in base-b notation,
    without any unnecessary leading zeroes.
    >>> number_to_string(-829, 10)
    "-829"
    >>> number_to_string(5, 3)
    "101"
    >>> number_to_string(0, 10)
    "0"
    """

import doctest
if __name__ == '__main__':
print(doctest.testmod(verbose=True))
print(sum_list([]))
print(sum_list([1,2,3,4,5]))
a = [[[6]]]
print(type(a[0][0][0]))
print(type(a))
print(len(a))
#print(a[0]+1)
print(productSum([[1,2],3,[4,5],[[[6]]]]))
print(powerset([1,2,3]))
print(subsequences([1,2,3]))
print(count)
b = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(b))