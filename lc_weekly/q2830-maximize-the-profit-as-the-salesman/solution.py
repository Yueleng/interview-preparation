# class Solution:
#     def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
#         # sort by end
#         offers.sort(key = lambda x: x[1])
#         #print(offers)
#         # dp[i]: max arrangement end as i
#         dp = [0 for i in range(n)]
#         for i in range(len(offers)):
#             offer = offers[i]
#             start = offer[0]
#             end = offer[1]
#             gold = offer[2]
#             dp[end] = max((max(dp[:start]) if start > 0 else 0) + gold, dp[end])
#             #print(dp)

#         return max(dp)


from ast import List
from bisect import bisect_right


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # sort by end
        offers.sort(key=lambda x: x[1])
        ends = [o[1] for o in offers]
        m = len(offers)
        dp = [0] * m
        for i in range(m):
            s, e, g = offers[i]
            j = bisect_right(ends, s - 1)
            bestPrevDp = dp[j - 1] if i > 0 else 0
            dp[i] = max(dp[i - 1] if i > 0 else 0, bestPrevDp + g)
        return dp[-1]
