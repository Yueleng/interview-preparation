from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortStr(_str: str) -> str:
            char_list = [*_str]
            char_list.sort()
            return "".join(char_list)

        result = []
        dp = defaultdict(list)

        for _str in strs:
            sort_str = sortStr(_str)
            if sort_str in dp:
                dp[sort_str].append(_str)
            else:
                dp[sort_str] = [_str]

        for _, strs in dp.items():
            result.append(strs)

        return result
