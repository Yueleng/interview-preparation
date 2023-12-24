class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        curr_score = s.count("1")

        for i in range(len(s) - 1):
            if s[i] == "0":
                curr_score += 1
            else:
                curr_score -= 1

            ans = max(ans, curr_score)

        return ans
