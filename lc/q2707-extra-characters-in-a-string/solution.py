from ast import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start : end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

    def minExtraChar2(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * len(s)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + (dp[start + 1] if start < n - 1 else 0)
            for end in range(start, n):
                curr = s[start : end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], (dp[end + 1] if end + 1 < n else 0))

        return dp[0]


# - convert dictionary into set for a faster `in` operation
# - dp[start]: minimum extra chars for subarray s[start:]
# - buttom-up-(right-to-left)-built dp
# -  to fill up a new dp[start]
# -    1. assign the value to the worst dp[start] = 1 + dp[start + 1]
# -    2. update dp[start] for a better result
