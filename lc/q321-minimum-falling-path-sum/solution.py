from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp
        n = len(matrix)
        dp = [[-1] * n for _ in range(n)]
        for row in range(n - 1, -1, -1):
            if row == n - 1:
                dp[row] = matrix[row]
            else:
                # i < n - 1
                for col in range(n):
                    _min = dp[row + 1][col]

                    if col > 0:
                        _min = min(dp[row + 1][col - 1], _min)
                    if col < n - 1:
                        _min = min(dp[row + 1][col + 1], _min)

                    dp[row][col] = matrix[row][col] + _min

        return min(dp[0])
