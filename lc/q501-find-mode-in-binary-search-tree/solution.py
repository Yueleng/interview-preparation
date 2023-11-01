from ast import List
from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dp = defaultdict(int)

        def traverse(node: Optional[TreeNode]):
            if node == None:
                return
            else:
                val = node.val
                dp[val] += dp[val] + 1
                traverse(node.left)
                traverse(node.right)

        traverse(root)

        max_vals = []
        max_cnt = 0
        for i in dp:
            if dp[i] > max_cnt:
                max_cnt = dp[i]
                max_vals = [i]
            elif dp[i] == max_cnt:
                max_vals.append(i)

        return max_vals
