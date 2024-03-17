# This is an input class. Do not edit.
import math
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode( head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    start = head
    faster = head
    count = 0
    while faster.next:

            count+=1
            faster=faster.next
    starting = 0
    middle =0
    middle=count/2

    while starting<middle:
        start = start.next
        starting+=1
    return start

def hasCycle(self, head: Optional[ListNode]) -> bool:
    faster = head
    slower = head
    if faster.next == slower:
        return True
    while faster.next.next:
        faster=faster.next.next
        slower = slower.next
        if faster == slower:
            return True
    return False


def insert(node,element):
    head = node
    temp = head
    while head:
        temp = head
        head = head.next
    head= LinkedList(value=element)
    temp.next=head


def printList(linkedList):
    head = linkedList
    while head:
        print(head.value,end=' ')
        head = head.next


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    current = head
    while current:
        if current.next and current.val == current.next.val:
            current.next=current.next.next
        else:
            current=current.next
    return head

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        temp = head
        while current:
            temp=current
            if current.val==val:
                if current.next:
                    temp.next=current.next
                    current=current.next

                else:
                    current=None
            current=current.next
        return head



def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    if linkedList is None:
        return None
    current = linkedList

    while current:
        if current.next and current.value == current.next.value:
            current.next=current.next.next

        else:
            current=current.next

    return linkedList

def reverseLinkedList(head):
    last = None
    current = head
    while current:
        temp = current.next
        current.next=last
        last=current
        current=temp
    head = last
    return head


def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  if not list1 and not list2:
      return None
  elif not list1:
      return list2
  elif not list2:
      return list1
  else:
      if list1.val<list2.val:
          list1.next=mergeTwoLists(list1.next,list2)
          return list1
      else:
          list2.next=mergeTwoLists(list1,list2.next)
          return list2

def deleteNode(node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        temp = node.next
        node.val=temp.val
        node.next=temp.next
        temp.next=None
        del temp




def rearrangeLinkedList(head:LinkedList, k)->LinkedList:
    # Write your code here.
    if head is None:
        return head
    beforeStart = None
    afterStart = None
    beforeEnd = None
    afterEnd = None
    while head is not None:
        nextNode = head.next
        head.next = None

        if head.value<k:
            if not beforeStart:
                beforeStart = head
                beforeEnd = beforeStart
            else:
                beforeEnd.next = head
                beforeEnd = head


        if head.value>k:
            if not afterStart:
                afterStart = head
                afterEnd = afterStart
            else:
                afterEnd.next = head
                afterEnd = head

        head = nextNode

    if not beforeStart:
        return afterStart
    beforeEnd.next = afterStart
    return beforeStart

def rearrangeLinkedListV2(node:LinkedList,k):
    head = node
    tail = node
    while node is not None:
        nextNode = node.next
        if node.value<k:
           node.next = head
           head = node
        else:
            tail.next = node
            tail = node
        node=nextNode
    tail.next = None
    return head








def removeKthNodeFromEnd(head, k):
    # Write your code here.
    length = 0
    current = head
    while current:
        current=current.next
        length+=1
    to_remove=length-k
    i=1


    current = head
    temp = current
    print(to_remove)
    if to_remove > 0:
        while i < to_remove:
            temp = current
            current = current.next
            i += 1

        if current.next:
            current.next = current.next.next if current.next.next is not None else None
        else:
            current = temp
    elif to_remove == 0:
        if current.next:
            current = current.next
            head = current
        else:
            head = None
    return head
def removeKthNodeFromEndV2(head, k):
    pass

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def countPair( head1, head2, n1, n2, x):
        """
        Counts the number of Pairs whose sum is equal to x
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        """


if __name__ == '__main__':
    l = LinkedList(1)
    insert(l,2)
    insert(l,3)




    printList(l)
    printList(l)

    printList(l)
    print()
    mid = middleNode(l)
    printList(l)
    print(mid.value)
    l = removeKthNodeFromEnd(l,1)
    printList(l)
