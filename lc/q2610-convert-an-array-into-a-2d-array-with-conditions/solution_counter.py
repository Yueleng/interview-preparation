from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ct = Counter(nums)
        rs = []
        while ct:
            l = []
            keys = list(ct.keys())
            for key in keys:
                ct[key] -= 1
                l.append(key)
                if ct[key] <= 0:
                    del ct[key]
            rs.append(l)

        return rs
