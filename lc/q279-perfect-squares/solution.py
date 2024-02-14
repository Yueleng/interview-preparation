class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i
            j = 1
            while j * j <= i:
                # bottom-up dp
                # when interating upon i
                # any j < i has been calculated and stored in dp[j]
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
