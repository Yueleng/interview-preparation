from collections import Counter, defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total_count = defaultdict(int)
        if len(words) == 1:
            return True

        for word in words:
            _count = Counter(word)
            for key in _count:
                total_count[key] += _count[key]

        length = len(words)
        for _, val in total_count.items():
            if val % length != 0:
                return False

        return True
