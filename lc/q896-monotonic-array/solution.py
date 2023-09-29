from ast import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        f1 = 0
        f2 = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                f1 = 1
            elif nums[i] > nums[i + 1]:
                f2 = 1

        return not (f1 == 1 and f2 == 1)
