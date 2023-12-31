from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp[i][j]: starting from ith job and j day left
        dp = [[None] * (d + 1) for _ in range(len(jobDifficulty) + 1)]
        n = len(jobDifficulty)

        def _minDifficulty(jobs_left: int, days_left: int):
            # total 9, 9 left, starting from 0
            # total 9, 8 left starting from 1

            if dp[jobs_left][days_left] != None:
                return dp[jobs_left][days_left]

            if jobs_left == days_left:
                dp[jobs_left][days_left] = sum(jobDifficulty[n - jobs_left :])
                return dp[jobs_left][days_left]

            if jobs_left < days_left:
                dp[jobs_left][days_left] = -1
                return dp[jobs_left][days_left]

            if days_left == 1:
                left_jobs = jobDifficulty[n - jobs_left :]
                dp[jobs_left][days_left] = max(left_jobs)
                return dp[jobs_left][days_left]

            # jobs_left > d:
            #

            min_cost = float("inf")
            for i in range(jobs_left - 1, days_left - 2, -1):
                first_day_jobs = jobDifficulty[n - jobs_left : n - i]
                cost = max(first_day_jobs)

                min_cost = min(cost + _minDifficulty(i, days_left - 1), min_cost)
                # print(i)
                # print(min_cost)

            dp[jobs_left][days_left] = min_cost

            return min_cost

        return _minDifficulty(n, d)
