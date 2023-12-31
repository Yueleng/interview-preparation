from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter("".join(words))
        for k, v in c.items():
            if v % len(words) != 0:
                return False
        return True
