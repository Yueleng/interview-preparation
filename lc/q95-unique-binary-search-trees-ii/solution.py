from ast import List
import itertools
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(l, r):
            if l == r:
                return [None]
            nodes = []

            # this question seems no need to cache the result
            for i in range(l, r):
                for lchild, rchild in itertools.product(
                    generate(l, i), generate(i + 1, r)
                ):
                    node = TreeNode(i + 1)
                    node.left, node.right = lchild, rchild
                    nodes.append(node)
            return nodes

        return generate(0, n) if n >= 1 else []
