# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start, tail = ListNode(0), ListNode(0)
        t1, t2 = start, tail
        while head:
            if head.val >= x:
                tail.next = ListNode(head.val)
                tail = tail.next
            else:
                start.next = ListNode(head.val)
                start = start.next
            head = head.next
        start.next = t2.next

        return t1.next
