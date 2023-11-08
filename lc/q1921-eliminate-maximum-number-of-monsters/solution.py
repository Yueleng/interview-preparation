from ast import List
from math import ceil


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        eta = [ceil(dist[i] / speed[i]) for i in range(n)]
        eta = sorted(eta)
        cur = eta[0]
        killed = 1
        acc = cur - 1
        for i in range(1, n):
            nxt = eta[i]
            if cur == nxt and acc == 0:
                return killed
            else:
                acc += nxt - cur

            acc -= 1
            cur = nxt
            killed += 1

        return killed
