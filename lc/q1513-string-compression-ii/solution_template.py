class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def count_to_len(cnt: int) -> int:
            return 1 + 3 if cnt >= 100 else 2 if cnt >= 10 else 1 if cnt >= 2 else 0

        n = len(s)
        dp = [[9999] * 110 for _ in range(110)]
        dp[0][0] = 0

        # dp[i][j]: the compression length of string: s[0:i] with j deletions
        # final solution should be dp[n][k] meaning the original string s with k deletions

        for i in range(1, n + 1):
            for j in range(0, k + 1):
                cnt, deletions = 0, 0
                for l in range(i, 0, -1):
                    if s[l - 1] == s[i - 1]:
                        cnt += 1
                    else:
                        deletions += 1

                    # j must be greater than deletions, otherwise, there is not enough deletion quota left
                    if j - deletions >= 0:
                        dp[i][j] = min(
                            dp[i][j], dp[l - 1][j - deletions] + count_to_len(cnt)
                        )

                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])

        return dp[n][k]
