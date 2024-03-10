from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        _max = 0
        freq = 0
        for num, count in counter.items():
            if count > _max:
                freq = count
                _max = count
            elif count == _max:
                freq += count
        return freq


# class Solution:
#     def maxFrequencyElements(self, nums: List[int]) -> int:
#         tmp = Counter(nums)
#         m = max(tmp.values())
#         return sum(map(lambda x: tmp[x], filter(lambda x: tmp[x] == m, tmp)))
