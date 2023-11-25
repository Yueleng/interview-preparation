from ast import List
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        # memo[i] = True if s[i:] can be segmented into words in wordSet
        # memo = [None] * len(s)

        @cache
        def backtrack(remain):
            if len(remain) == 0:
                return True

            else:
                # iterate through all possible candidates
                for i in range(len(remain)):
                    candidate = remain[: i + 1]
                    if candidate in wordSet:
                        if i + 1 == len(s):
                            return True
                        else:
                            if backtrack(remain[len(candidate) :]):
                                return True

                return False

        return backtrack(s)
