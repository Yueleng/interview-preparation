from ast import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(_root: Optional[TreeNode]) -> List[int]:
            if not _root:
                return []
            else:
                return inorder(_root.left) + [_root.val] + inorder(_root.right)

        return inorder(root)
        # if not _root.left and not _root.right:
        #     return [_root.val]
        # elif:
