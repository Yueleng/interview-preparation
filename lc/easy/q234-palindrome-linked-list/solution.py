# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []

        cur, length = head, 0

        while cur:
            arr.append(cur)
            cur, length = cur.next, length + 1

        left, right = 0, length - 1

        while left < right:
            if arr[left].val != arr[right].val:
                return False
            left += 1
            right -= 1

        return True
