from operator import itemgetter
from typing import List


def value_comparator(x1, x2):
    order1 = x1 + x2
    order2 = x2 + x1
    return max(int(order1), int(order2))

def largest_number_can_be_formed(l:List[int]):
    def value_comparator(x1,x2):
        order1 = x1+x2
        order2 = x2+x1
        return max(int(order1),int(order2))

    out = ""
    agenda =  " ".join(x for x in l)
    visited = set()

    for index in range(len(l)):
        if












def main():
    largest_number = [9,5,3,34,30,321]
    "".join(str(x) for x1,x2 in zip(largest_number,largest_number[1:]) if x1==value_comparator(x1,x2)
