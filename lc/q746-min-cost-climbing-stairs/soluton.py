from ast import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}

        def cost_start_from(idx: int) -> int:
            if idx in dp:
                return dp[idx]
            if idx >= len(cost):
                return 0
            if idx == len(cost) - 1:
                return cost[idx]
            else:
                a = cost_start_from(idx + 1)
                dp[idx + 1] = a
                b = cost_start_from(idx + 2)
                dp[idx + 2] = b

                dp[idx] = min(a, b) + cost[idx]
                return dp[idx]

        return min(cost_start_from(0), cost_start_from(1))
