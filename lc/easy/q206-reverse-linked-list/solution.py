from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        cur, length = head, 0

        while cur:
            arr.append(cur)
            cur, length = cur.next, length + 1

        if length == 0:
            return None

        for idx in range(length - 1, 0, -1):
            arr[idx].next = arr[idx - 1]

        arr[0].next = None

        return arr[length - 1]
