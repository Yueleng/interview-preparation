from ast import List
import collections
import math


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        digitsNum = collections.defaultdict(list)
        MIN = -math.inf

        def getMaxDigit(num):
            def getMaxDigitsRecur(remain, _max):
                if remain < 10:
                    return max(_max, remain)
                return getMaxDigitsRecur(remain // 10, max(remain % 10, _max))

            return getMaxDigitsRecur(num, 0)

        def getMaxSum(nums):
            if len(nums) < 2:
                return MIN
            _max = max(nums[0], nums[1])
            sec_max = min(nums[0], nums[1])

            for i in range(2, len(nums)):
                if nums[i] >= _max:
                    sec_max = _max
                    _max = nums[i]
                elif nums[i] < _max and nums[i] > sec_max:
                    sec_max = nums[i]

            return sec_max + _max

        # generate digitsNum
        for i in range(len(nums)):
            digitsNum[getMaxDigit(nums[i])].append(nums[i])

        _max = MIN
        for digit in digitsNum:
            _maxSum = getMaxSum(digitsNum[digit])
            if _maxSum > _max:
                _max = _maxSum

        return -1 if _max == MIN else _max
