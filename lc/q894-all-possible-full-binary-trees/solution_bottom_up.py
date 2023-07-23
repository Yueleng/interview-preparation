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
    def allPossibleFBT(self, _n: int):
        # Any full binary trees should contain odd number of nodes
        # therefore, if n is even, return 0
        if _n % 2 == 0:
            return []
        # for all odd n that are less than n, store all FBTs
        trees_all = collections.defaultdict(list)

        # when there is one node, only one tree is available
        trees_all[1] = [TreeNode(0)]
        for n in range(3, _n + 1, 2):
            for k in range(1, n, 2):
                # trees with k nodes on the left
                # trees with n - k - 1 nodes on the right
                # consider all potential pairs
                for tree1, tree2 in itertools.product(
                    trees_all[k], trees_all[n - k - 1]
                ):
                    tree = TreeNode(0)
                    tree.left = tree1
                    tree.right = tree2
                    trees_all[n].append(tree)

        # print(trees_all[_n])
        return trees_all[_n]


if __name__ == "__main__":
    solution = Solution()
    solution.allPossibleFBT(7)
