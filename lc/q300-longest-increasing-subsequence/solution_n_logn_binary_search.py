from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        # for each num, find the first tail that is larger than num
        for num in nums:
            i, j = 0, size
            while i != j:
                # m <- floor
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            size = max(i + 1, size)
        return size
