from ast import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * len(s)

        for end in range(n):
            dp[end] = 1 + (dp[end - 1] if end > 0 else 0)
            for start in range(end + 1):
                curr = s[start : end + 1]
                if curr in dictionary_set:
                    dp[end] = min(dp[end], (dp[start - 1] if start > 0 else 0))
        return dp[-1]


# - convert dictionary into set for a faster `in` operation
# - dp[end]: minimum extra chars for subarray s[:end+1]
# - buttom-up-(left-to-right)-built dp
# -  to fill up a new dp[end]
# -    1. assign the value to the worst dp[end] = 1 + dp[end - 1]
# -    2. update dp[end] for a better result
