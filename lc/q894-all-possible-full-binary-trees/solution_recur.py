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
        if n == 1:
            return [TreeNode()]

        res = []

        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)

            # equivalent with
            # for l, r in itertools.product(left, right):
            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)

        return res

    # faster way
    # def allPossibleFBT2(self, n: int) -> List[Optional[TreeNode]]:
    def allPossibleFBT2(self, n: int):
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode())

        def possibleFBTRecur(_n):
            if len(dp[_n]) > 0:
                return dp[_n]

            for i in range(1, _n, 2):
                j = _n - i - 1
                left = possibleFBTRecur(i)
                right = possibleFBTRecur(j)
                for l, r in itertools.product(left, right):
                    root = TreeNode(0, l, r)
                    dp[_n].append(root)
            return dp[_n]

        return possibleFBTRecur(n)


# Time Complexity and Space Complexity both bad
