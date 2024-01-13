from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)

        opt = 0
        for char in s_count:
            if char in t_count:
                opt += abs(s_count[char] - t_count[char])
                del t_count[char]
            else:
                opt += s_count[char]

        for char in t_count:
            opt += t_count[char]

        return int(opt // 2)
