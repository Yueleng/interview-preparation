class Solution:
    def climbStairs(self, n: int) -> int:
        # how many stairs for n
        dp = [0] * n

        for i in range(n):
            if i == 0:
                dp[i] = 1
                continue
            if i == 1:
                dp[i] = 2
                continue

            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n - 1]
