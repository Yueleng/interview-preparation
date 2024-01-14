# DFS
# Consider all the leaves of a binary tree.
# From left to right order, the values of those leaves form a leaf value sequence.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaves(node: Optional[TreeNode]):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [node.val]
            return findLeaves(node.left) + findLeaves(node.right)

        return findLeaves(root1) == findLeaves(root2)
