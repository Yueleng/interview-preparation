class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)

        if n < d:
            return -1

        dp = [[float("inf")] * (d + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        # incremental expand i jobs
        for i in range(1, n + 1):
            # calculate all k days under total i jobs
            for k in range(1, min(d, i) + 1):
                mx = jobDifficulty[i - 1]
                # j has its own lower bound: k
                # since we have to spare the rest of k - 1 jobs for k - 1 days
                for j in range(i, k - 1, -1):
                    mx = max(mx, jobDifficulty[j - 1])
                    dp[i][k] = min(dp[i][k], dp[j - 1][k - 1] + mx)

        return dp[n][d]


# Given an array, minimze the maximum sum of a subarray of size k
# dp[i][k]: Given an array s[0:i] (including),
# minimize the "the sum of the each maximum subarray of size k"
# {XXXXXXX} [j xxxx i]
