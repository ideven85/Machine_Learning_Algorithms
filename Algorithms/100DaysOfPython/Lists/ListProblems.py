from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListProblems:

    def insert(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current = head
        while current:
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

    if '__name__' == '__main__':
        pass

