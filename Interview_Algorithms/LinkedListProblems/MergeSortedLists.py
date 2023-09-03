from math import *
from collections import *
from sys import *
from os import *

import sys
from sys import stdin

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(list1, list2):
    # Write your code here.
    if not list1 and not list2:
      return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    else:
        if list1.data<list2.data:
            list1.next=sortTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=sortTwoLists(list1,list2.next)
            return list2










def ll(arr):
    
    if len(arr)==0:
        return None
    
    head = Node(arr[0])
    last = head
    
    for data in arr[1:]:
        
        last.next = Node(data)
        last = last.next
        
    return head

def printll(head):
    
    while head:
        
        print(head.data, end=' ')
        
        head = head.next
        
    print(-1)

    

t = int(sys.stdin.readline().strip())

for i in range(t):
    
    arr1=list(map(int, sys.stdin.readline().strip().split(" ")))
    arr2=list(map(int, sys.stdin.readline().strip().split(" ")))
    
    l1 = ll(arr1[:-1])
    l2 = ll(arr2[:-1])
    
    l = sortTwoLists(l1, l2)
    
    printll(l)

