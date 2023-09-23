from ast import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words_sorted = sorted(words, key=len)
        for w in words_sorted:
            dp[w] = max(dp[w[:i] + w[i + 1 :]] + 1 for i in range(len(w)))
        return max(dp.values())
