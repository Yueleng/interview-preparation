from ast import List
from math import inf

# bottom-up


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        # (n+1) * (n+1) matrix
        # dp[i][j] start pick up from index i with j time(must use up), what is the minimum cost you can achieve
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # last row is not pickable, set as inf
        for j in range(n - 1, -1, -1):
            dp[n][j] = inf

        # start from last row
        for i in range(n - 1, -1, -1):
            # start from 1 remaining
            for remain in range(1, n + 1):
                # set current ith wall by paid-painter
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                # set current ith wall by free-painter
                dont_paint = dp[i + 1][remain]

                dp[i][remain] = min(paint, dont_paint)

        return dp[0][n]
