from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # generate all trees with nodes from start to end (excluding end)
        def generate(start, end):
            if start == end:
                return [None]
            if end - start == 1:
                return [TreeNode(start)]
            else:
                res = []
                for i in range(start, end):
                    # all left subtrees with nodes from start to i - 1
                    left = generate(start, i)

                    # all right subtrees with nodes from i + 1 to end - 1
                    right = generate(i + 1, end)

                    for l in left:
                        for r in right:
                            root = TreeNode(i + 1)
                            root.left, root.right = l, r
                            res.append(root)
            return res

        return generate(1, n + 1)
