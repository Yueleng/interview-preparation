class Solution:
    def maxScore(self, s: str) -> int:
        _max = -1
        for pos_idx in range(1, len(s)):
            left_str = s[:pos_idx]
            right_str = s[pos_idx:]
            _max = max(_max, left_str.count("0") + right_str.count("1"))
        return _max
