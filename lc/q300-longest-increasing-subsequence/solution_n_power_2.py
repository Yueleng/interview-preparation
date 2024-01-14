# Longest Increasing Subsequence
# url: https://leetcode.com/problems/longest-increasing-subsequence/
# desc: Given an unsorted array of integers, find the length of longest increasing subsequence.
#       Example:
#           Input: [10,9,2,5,3,7,101,18]
#           Output: 4
#           Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#       Note:
#           There may be more than one LIS combination, it is only necessary for you to return the length.
#           Your algorithm should run in O(n2) complexity.
#       Follow up: Could you improve it to O(n log n) time complexity?

# Time: O(n^2)
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = longest increasing subsequence ending at nums[i]
        if not nums:
            return 0

        dp = [1] * len(nums)
        # in this loop, calculate dp[i], and do[i] will never be updated later
        for i in range(len(nums)):
            # update possible i
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
