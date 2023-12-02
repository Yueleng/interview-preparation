from ast import List
from collections import defaultdict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_stat = defaultdict(int)
        for char in chars:
            chars_stat[char] += 1

        def if_good(cand: str) -> bool:
            cand_stat = defaultdict(int)
            for char in cand:
                cand_stat[char] += 1

            for char in cand_stat:
                if cand_stat[char] > chars_stat[char]:
                    return False

            return True

        _sum = 0
        for word in words:
            if if_good(word):
                _sum += len(word)

        return _sum
