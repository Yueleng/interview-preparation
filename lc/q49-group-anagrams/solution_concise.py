from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for _str in strs:
            sorted_str = "".join(sorted(_str))
            anagram_map[sorted_str].append(_str)

        return list(anagram_map.values())
