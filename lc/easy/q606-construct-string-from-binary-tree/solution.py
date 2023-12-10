# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def genStr(_root: Optional[TreeNode]) -> str:
            if not _root.left and not _root.right:
                return str(_root.val)
            # have left but no right
            elif _root.left and not _root.right:
                return str(_root.val) + "(" + genStr(_root.left) + ")"
            # have left and right
            elif _root.left and _root.right:
                return (
                    str(_root.val)
                    + "("
                    + genStr(_root.left)
                    + ")("
                    + genStr(_root.right)
                    + ")"
                )
            # left is None, right not None
            # not _root.left and _root.right
            else:
                return str(_root.val) + "()(" + genStr(_root.right) + ")"

        return genStr(root)
