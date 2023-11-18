class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 36

        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if first[curr] == -1:
                first[curr] = i

            last[curr] = i

        ans = 0

        for i in range(26):
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            ans += len(between)

        return ans
