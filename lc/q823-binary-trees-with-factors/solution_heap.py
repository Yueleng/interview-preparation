from ast import List
from heapq import heappop, heappush
from itertools import product


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        As = set(A)  # set for O(1)
        pq = []  # min heap
        modular = 1_000_000_007

        for x, y in product(A, A):
            if x * y in As:
                heappush(pq, (x * y, x, y))

        cnt = {x: 1 for x in A}
        while pq:
            z, x, y = heappop(pq)
            cnt[z] += (cnt[x] * cnt[y]) % modular

        return sum(cnt.values()) % modular
