from ast import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        _max = 0
        for i in range(n // 2):
            _max = max(_max, nums[i] + nums[n - 1 - i])
        return _max
