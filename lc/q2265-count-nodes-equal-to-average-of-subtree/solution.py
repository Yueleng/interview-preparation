# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def sum_n_count(node):
            nonlocal result
            if not node:
                return (0, 0)

            left_sum, left_count = sum_n_count(node.left)
            right_sum, right_count = sum_n_count(node.right)

            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            if curr_sum // curr_count == node.val:
                result += 1

            return curr_sum, curr_count

        sum_n_count(root)

        return result
