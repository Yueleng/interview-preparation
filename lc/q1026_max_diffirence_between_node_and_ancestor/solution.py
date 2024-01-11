# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def searchMaxDiff(
            prev_max: int, prev_min: int, current_node: Optional[TreeNode]
        ) -> int:
            if not current_node:
                return prev_max - prev_min
            else:
                new_max = max(prev_max, current_node.val)
                new_min = min(prev_min, current_node.val)
                return max(
                    searchMaxDiff(new_max, new_min, current_node.left),
                    searchMaxDiff(new_max, new_min, current_node.right),
                )

        return searchMaxDiff(root.val, root.val, root)
