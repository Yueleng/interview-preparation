# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from ast import List
from collections import deque
from typing import Optional


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            cur_levl_max = float("-inf")
            next_levl_nodes = []
            for node in queue:
                if node.left:
                    next_levl_nodes.append(node.left)
                if node.right:
                    next_levl_nodes.append(node.right)
                if node.val > cur_levl_max:
                    cur_levl_max = node.val
            res.append(cur_levl_max)
            queue = deque(next_levl_nodes)
        return res
