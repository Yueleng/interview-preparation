# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(node):
            sm = 2 * node.val + (dfs(node.next) if node.next else 0)
            node.val = sm % 10
            return sm // 10

        return ListNode(1, head) if dfs(head) else head
