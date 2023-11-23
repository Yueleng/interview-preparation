class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # n: arr has exactly n integers
        # m: maximum of all the ele(s) in arr
        # k: num of gaps (num of comparisons)

        if m < k:
            return 0

        # [[1,1,1,...1], [0,0,0,...,0], ..., [0,0,0,...,0]]
        # dim(dp) = k * m
        dp = [[1] * m] + [[0] * m for _ in range(k - 1)]
        mod = 10**9 + 7

        # loop through all ele(s) in array
        for _ in range(n - 1):
            # loop through gaps
            for i in range(k - 1, -1, -1):
                cur = 0
                # loop through max_val
                for j in range(m):
                    # dp[i][j]: numOfArrays for maxVal == j and gaps == i
                    dp[i][j] = (dp[i][j] * (j + 1) + cur) % mod
                    if i:
                        cur = (cur + dp[i - 1][j]) % mod

        # return the sum of last row, (sum over all possible maxVals)
        return sum(dp[-1]) % mod


# 1 0 0
# 1 1 1
# 1 2 2
# 1 3 3
# 0 0 1
# 0 1 2
# 0 2 3
# 0 3 4
# 1 0 0
# 1 1 3
# 1 2 9
# 1 3 18
# 0 0 1
# 0 1 4
# 0 2 9
# 0 3 16
