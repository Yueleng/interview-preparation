# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        def connect(left_tail_node, mid_head_node, mid_tail_node, right_head):
            if left_tail_node:
                left_tail_node.next = mid_head_node
            if right_head:
                mid_tail_node.next = right_head

        count = 0
        left_tail_node = head
        pointer = head
        right_head = None
        mid_tail_node = None
        mid_head_node = None
        while pointer:
            count += 1

            if count < left - 1:
                left_tail_node = left_tail_node.next
            # elif count == left - 1:
            # left_tail_node standstill; no action

            elif count == left:
                if left == 1:
                    left_tail_node = None
                mid_tail_node = ListNode(pointer.val)
                mid_head_node = mid_tail_node
            elif count < right:
                mid_head_node = ListNode(pointer.val, mid_head_node)
            elif count == right:
                mid_head_node = ListNode(pointer.val, mid_head_node)
                if pointer.next:
                    right_head = pointer.next
            elif count == right + 1:
                right_head = pointer
            pointer = pointer.next
        connect(left_tail_node, mid_head_node, mid_tail_node, right_head)
        print(left_tail_node)
        print(mid_head_node)
        return head if left_tail_node != None else mid_head_node
