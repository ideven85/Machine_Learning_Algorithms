from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListProblems:

    def insert(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(0)
        current = output
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val+carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
            l1=l1.next
            l2=l2.next
        while l1:
            total = l1.val + carry
            digit = total%10
            carry = total//10
            current.next = ListNode(digit)
            current = current.next
            l1=l1.next
        while l2:
            total = l2.val + carry
            digit = total % 10
            carry = total // 10
            current.next = ListNode(digit)
            current = current.next
            l2 = l2.next
        if carry:
            current.next = ListNode(carry)
        return output.next


    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        #next_node=head.next
        prev = None
        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head
            next_node = head.next.next  # Step 2
            head.next.next = head  # Step 1

            head.next = next_node  # Step 6
            head = next_node


        return temp
    def printList(self, head: Optional[ListNode]) -> None:
        current = head
        while current:
            print(current.val,end=' ')
            current=current.next
        print()

if __name__ == '__main__':

        head = ListNode(1)

        l = ListProblems()
        l.insert(head, 2)
        l.insert(head,3)
        l.insert(head,4)

        l.printList(head)
        head=l.swapPairs(head)
        l.printList(head)


