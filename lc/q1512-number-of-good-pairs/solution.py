from ast import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1

        sum = 0
        for key in dct:
            if dct[key] >= 2:
                sum += dct[key] * (dct[key] - 1) // 2

        return sum
