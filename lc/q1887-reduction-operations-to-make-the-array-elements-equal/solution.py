from ast import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        addOn = 0
        nums.sort(reverse=True)
        result = 0
        for i in range(n):
            if i > 0 and nums[i - 1] > nums[i]:
                result += addOn
            addOn += 1
        return result
