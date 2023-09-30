from ast import List
import math


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        second_largest = -math.inf
        stck = []

        # Try to find nums[i] < second_largest < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_largest:
                return True

            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
                # this will ensure second_largest < stck[-1] for next iteration
                second_largest = stck.pop()

            stck.append(nums[i])

        return False
