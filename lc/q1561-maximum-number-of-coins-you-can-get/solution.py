from ast import List
from collections import deque


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        dq = deque(piles)
        n3 = len(piles)
        n = n3 // 3
        result = 0
        for _ in range(n):
            dq.pop()
            second_largest = dq.pop()
            dq.popleft()
            result += second_largest
        return result
