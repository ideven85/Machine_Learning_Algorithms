from os import *
from sys import *
from collections import *
from math import *

# Following is the List Node Class Structure:
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None

def insert(node,element):
    head = node
    temp = head
    while head:
        temp = head
        head = head.next
    head= Node(data==element)
    temp.next=head
    
def printList(linkedList):
    head = linkedList
    while head:
        print(head.data,end=' ')
        head = head.next
def rearrangeList(head:Node):
    # Write your code here.
    """Given the head of a list rearrange it so that the last element occurs after first element

    Args:
        head (Node): Head of a list
    """
    current = head
    n = 0
    while current.next!=None:
        current=current.next
        n+=1
    #print(current.data)
    #a = input()
    n+=1
    if n==1:
        return head
    temp=head.next
    head.next=current
    current.next=temp
    current=head
    for i in range(n-1):
        current=current.next
    current.next=None
    return head


root = Node(1)
current=root
current.next=Node(2)
current=current.next
current.next=Node(3)
current=current.next
current.next=Node(4)
printList(root)
rearrangeList(root)
print()
printList(root)
    
    
    
        
    