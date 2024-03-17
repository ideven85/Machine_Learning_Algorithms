from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Main:


    def insert(self, head, val):
        current=head
        if not head:
            head = ListNode(val)
        else:
            while current.next:
                current=current.next
            current.next=ListNode(val)
            current=current.next
            current.next=None
        return head



    def printList(self,head):
        while head:
            print(head.val,end=' ')
            head=head.next
        print()

    def length(self,head):
        size=0
        while head:
            size+=1
            head=head.next
        return size
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        p=head
        n=1
        while p.next:
            n+=1
            p=p.next
        p.next=head
        k=k%n
        for i in range(n-k):
            p=p.next
        head=p.next
        p.next=None
        return head



    def swapPairs(self,head:Optional[ListNode])->Optional[ListNode]:

        if not head or not head.next:
            return head
        else:
            """
             swapped=head.next;
            head.next=swapped.next;
            swapped.next=head;
            head = swapped;
            """
            swapped=head.next
            head.next,swapped.next=swapped.next,head

            head=swapped
            head.next.next=self.swapPairs(head.next.next)

            return head





    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

    def rearrangeList(self,head):
        # Write your code here.
        """Given the head of a list rearrange it so that the last element occurs
         after first element

        Args:
            head (Node): Head of a list
        """
        current = head
        n = 0
        while current.next :
            current = current.next
            n += 1
        # print(current.data)
        # a = input()
        n += 1
        if n == 1:
            return head
        temp = head.next
        head.next = current
        current.next = temp
        current = head
        for i in range(n - 1):
            current = current.next
        current.next = None
        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not  list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val<list2.val:
                list1.next=self.mergeTwoLists(list1.next,list2)
                return list1
            else:
                list2.next=self.mergeTwoLists(list1,list2.next)
                return list2









if __name__ == '__main__':
    main = Main()

    head = ListNode(10)
    current=head
    head=main.insert(head,20)
    head=main.insert(head,20)
    head=main.insert(head,15)
    head=main.insert(head,25)
    head=main.insert(head,30)
    head=main.insert(head,12)
    main.printList(head)
    head=main.rotateRight(head,2)
    main.printList(head)
    head=main.rearrangeList(head)
    main.printList(head)
    head=main.swapPairs(head)
    main.printList(head)


