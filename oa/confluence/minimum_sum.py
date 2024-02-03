import heapq
import math
from typing import List


def minSum(num: List[int], k: int) -> int:
    num = [(-1) * i for i in num]
    heapq.heapify(num)
    for _ in range(k):
        # n = -5
        n = heapq.heappop(num)
        # math.floor(-5 / 2) = math.floor(-2.5) = -3
        n = math.floor(n / 2)
        heapq.heappush(num, n)

    return -sum(num)
