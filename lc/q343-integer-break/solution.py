from collections import defaultdict


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = defaultdict(int)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        def getDp(n):
            if n in dp:
                return dp[n]
            else:
                _max = 1
                for i in range(2, n):
                    _max = max(_max, i * getDp(n - i))
                dp[n] = _max
                # print("n: ", n)
                # print("max: ", _max)
                return _max

        if n <= 3:
            return dp[n] - 1

        else:
            return getDp(n)
