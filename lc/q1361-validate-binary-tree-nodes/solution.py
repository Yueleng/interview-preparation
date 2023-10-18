from ast import List
from collections import deque


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        root = 0
        childrenNodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in childrenNodes:
                root = i
        visited = set()
        _deque = deque([root])

        while len(_deque) > 0:
            current_node = _deque.popleft()
            if current_node in visited:
                return False
            visited.add(current_node)

            left = leftChild[current_node]
            right = rightChild[current_node]

            if left > -1:
                _deque.append(left)

            if right > -1:
                _deque.append(right)

        return True if len(visited) == n else False
