from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        n = len(s)
        for i in range(n):
            char = s[i]
            if counter[char] == 1:
                return i

        return -1
