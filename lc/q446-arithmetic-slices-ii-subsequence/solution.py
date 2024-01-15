from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]

        # dp[i][diff] is the number of arithmetic slices ending at i with difference diff
        for i in range(1, n):
            # loop through all the previous elements
            for j in range(i):
                # calculate the difference between nums[i] (new number)
                # and nums[j] (previous number)
                diff = nums[i] - nums[j]
                # increase by 1 the number of arithmetic slices ending at i with difference diff
                dp[i][diff] += 1
                # increase the total count by the number of arithmetic slices ending at j
                # with difference diff, if diff is already in dp[j]
                if diff in dp[j]:
                    # by adding dp[j][diff] to dp[i][diff], we are extending the arithmetic slices
                    # ending at i with difference by diff
                    dp[i][diff] += dp[j][diff]
                    # increase the total count by the number of arithmetic slices ending at j
                    total_count += dp[j][diff]

        return total_count


# examples and explanations
# nums = [2, 4, 6, 8, 10]
# dp = [{}, {}, {}, {}, {}]
# after i = 1 (val = 4) => dp = [{}, {2: 1}, {}, {}, {}] and total_count = 0
# after i = 2 (val = 6) => dp = [{}, {2: 1}, {2: 2, 4: 1}, {}, {}] and total_count = 1
# after i = 3 (val = 8) => dp = [{}, {2: 1}, {2: 2, 4: 1}, {2: 3, 4: 1, 6: 1}, {}] and total_count = 3
# after i = 4 =>
# dp = [{}, {2: 1}, {2: 2, 4: 1}, {2: 3, 4: 1, 6: 1}, {2: 4, 4: 2, 6: 1, 8: 1}] and total_count = 7
#
