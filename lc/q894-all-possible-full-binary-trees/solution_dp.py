from ast import List
import collections
import itertools
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def allPossibleFBT(self, _n: int) -> List[Optional[TreeNode]]:
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:
            return []

        # initialization of dp
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode())

        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)
        return dp[n]

    # equivalent
    # def allPossibleFBT2(self, n: int) -> List[Optional[TreeNode]]:
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:
            return []

        # initialization of dp
        dp = [[] for _ in range(n + 1)]

        dp[1].append(TreeNode())

        for _n in range(3, n + 1, 2):
            # purpose in this loop: fill up dp[_n]
            for i in range(1, _n, 2):
                j = _n - 1 - i
                for left, right in itertools.product(dp[i], dp[j]):
                    # left = dp[i]
                    # right = dp[j]
                    root = TreeNode(0, left, right)
                    dp[_n].append(root)

        return dp[n]
