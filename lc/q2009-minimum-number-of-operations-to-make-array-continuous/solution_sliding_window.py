from ast import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))

        # kept_count: how many were kept the same
        kept_count = ii = 0
        for i, x in enumerate(nums):
            # ii base
            if x - nums[ii] >= n:
                ii += 1
            kept_count = max(kept_count, i - ii + 1)
        return n - kept_count
