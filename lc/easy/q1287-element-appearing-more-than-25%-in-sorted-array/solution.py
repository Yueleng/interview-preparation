from typing import List
from math import ceil


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        thold = len(arr) * 0.25 + 1 if len(arr) % 4 == 0 else ceil(len(arr) * 0.25)

        acc = 1
        for i in range(1, len(arr)):
            _int = arr[i]
            _prev_int = arr[i - 1]
            if _int == _prev_int:
                acc += 1
                if acc >= thold:
                    return _int
            else:
                acc = 1

        return arr[0]
