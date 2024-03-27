from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        product = 1

        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and left <= r:
                product /= nums[left]
                left += 1
            res += r - left + 1

        return res
