from bisect import bisect
from typing import List


class Solution:
    def lengthOfLIST(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            # find the index of the first element that is larger than num
            insert_index = bisect.bisect_left(dp, num)

            if insert_index == len(dp):
                dp.append(num)
            else:
                dp[insert_index] = num
        return len(dp)
