from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occs = set()
        counter = Counter(arr)
        for _, val in counter.items():
            if val in occs:
                return False
            occs.add(val)

        return True
