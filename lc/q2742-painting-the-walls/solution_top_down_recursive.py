from ast import List
from functools import cache
from math import inf


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        # start pick up from index i with remain time(must use up), what is the minimum cost you can achieve
        @cache
        def dp(i, remain):
            # if we don't have enough remain, return 0
            if remain <= 0:
                return 0
            # if we reached last row (no choice at all, never pick this row)
            if i == n:
                return inf

            # pick up wall i and apply paid painter
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            # pick up wall i and apply un-paid painter
            dont_paint = dp(i + 1, remain)
            # get minimum of the two choice
            return min(paint, dont_paint)

        # start pick up from index 0 with remain: n time unit, what is the minumum cost you can achieve
        return dp(0, n)
