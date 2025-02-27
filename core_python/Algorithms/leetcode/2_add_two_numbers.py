# Definition for singly-linked list.
import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(val)
    return head


def create_list(head, val):
    if head is None:
        head = ListNode(val)
        head.next = None
    else:
        head.next = ListNode(val)
        head = head.next
        # head.next=None
    return head


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    last = None
    current = head
    while current:
        temp = current.next
        current.next = last
        last = current
        current = temp
    head = last
    return head


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=",")
        head = head.next
    print()


class Solution:

    def reverse(self, head):
        prev = None
        current = head
        while current:
            prev, prev.next, current = current, prev, current.next
        return prev

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        else:
            l1 = self.reverse(l1)
            l2 = self.reverse(l2)
            output = ListNode(0)
            current = output
            carry = 0
            while l1 and l2:
                total = l1.val + l2.val + carry
                digit = total % 10
                carry = total // 10
                current.next = ListNode(digit)
                current = current.next
                l1 = l1.next
                l2 = l2.next
            while l1:
                total = l1.val + carry
                digit = total % 10
                carry = total // 10
                current.next = ListNode(digit)
                current = current.next
                l1 = l1.next
            while l2:
                total = l2.val + carry
                digit = total % 10
                carry = total // 10
                current.next = ListNode(digit)
                current = current.next
                l2 = l2.next
            if carry:
                current.next = ListNode(carry)

            return self.reverse(output.next)

    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        out = ListNode()
        if not l1 and not l2:
            return out
        elif not l1:
            self.add_two_numbers(out, l2)
        elif not l2:
            self.add_two_numbers(l1, out)
        else:
            out.val = (l1.val + l2.val) % 10
            out = out.next
            self.add_two_numbers(l1.next, l2.next)
        return out


def main():
    sol = Solution()
    head1 = ListNode(1)
    insert(head1, 2)
    insert(head1, 3)
    head2 = ListNode(2)
    insert(head2, 9)
    insert(head2, 9)
    x = sol.addTwoNumbers(head1, head2)

    print_list(x)


if __name__ == "__main__":
    main()
