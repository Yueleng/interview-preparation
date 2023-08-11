from ast import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != math.inf else -1
