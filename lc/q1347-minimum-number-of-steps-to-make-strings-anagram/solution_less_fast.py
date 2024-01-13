from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        s_counter = Counter(s)
        t_counter = Counter(t)

        for char in set(t):
            diff = t_counter[char] - (0 if char not in s_counter else s_counter[char])
            res += diff if diff > 0 else 0

        return res
