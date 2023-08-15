from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = None
        right = None

        left_pointer = left
        right_pointer = right

        while head:
            value = head.val

            if value < x:
                node = ListNode(value)
                # first node
                if left_pointer == None:
                    left_pointer = node
                    left = node
                else:
                    left_pointer.next = node
                    left_pointer = node
            else:  # value >= x:
                node = ListNode(value)
                if right_pointer == None:
                    right_pointer = node
                    right = node
                else:
                    right_pointer.next = node
                    right_pointer = node

            head = head.next

        if left_pointer:
            left_pointer.next = right

        return left if left != None else right
