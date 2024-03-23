# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        cur, cur_idx = list1, 0
        a_node = None
        b_node = None
        while cur:
            if cur_idx + 1 == a:
                a_node = cur

            if cur_idx - 1 == b:
                b_node = cur

            cur = cur.next
            cur_idx += 1

        lst2_tail = None
        cur = list2
        while cur and cur.next:
            cur = cur.next

        lst2_tail = cur

        # connect
        a_node.next = list2
        lst2_tail.next = b_node

        return list1
