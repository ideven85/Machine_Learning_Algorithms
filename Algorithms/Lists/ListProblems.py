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

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
        return output.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        # next_node=head.next
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
            print(current.val, end=" ")
            current = current.next
        print()

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

    def length(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        return 1 + self.length(head.next)

    def reverse(self, head):
        prev = None
        current = head
        while current:
            prev, prev.next, current = current, prev, current.next
        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        fast = head.next
        slow = head
        # Catch the Middle of List (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Cut Middle of list then Reverse it
        rev = self.reverse(slow.next)
        slow.next = None

        while rev:
            h_next = head.next
            r_next = rev.next
            head.next = rev
            rev.next = h_next
            rev = r_next
            head = h_next

    def reorderListV2(self, head: Optional[ListNode]) -> None:
        """
                ou are given the head of a singly linked-list.
                The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes.
         Only nodes themselves may be changed.
        """
        if not head:
            return
        reversed_list = self.reverseList(head)
        # raise NotImplementedError("Please Implement me")
        current = head

        length = self.length(head)
        while head and head.next:
            head.next = reversed_list
            head.next = head.next.next
            reversed_list = reversed_list.next.next
            head = head.next.next


"""
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        
        if(head == null || head.next == null) return;

        ListNode slow = head, fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }


        ListNode prev = null, next = null;
        while(slow != null) {
            next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }

        ListNode firstHf = head;
        ListNode secondHf = prev;

        while(secondHf.next != null) {
            next = firstHf.next;
            prev = secondHf.next;

            firstHf.next = secondHf;
            secondHf.next = next;

            firstHf = next;
            secondHf = prev;
        }
    }
}
"""


if __name__ == "__main__":

    head = ListNode(1)

    l = ListProblems()
    l.insert(head, 2)
    l.insert(head, 3)
    l.insert(head, 4)

    l.printList(head)
    # head=l.swapPairs(head)
    # l.printList(head)
    # reversed_list=l.reverseList(head)
    # l.printList(reversed_list)
    print()
    l.reorderList(head)
    l.printList(head)
