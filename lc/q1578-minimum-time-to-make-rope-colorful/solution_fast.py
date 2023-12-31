from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        res = 0
        cost = [neededTime[0]]
        cur = colors[0]
        for i in range(len(colors) - 1):
            if cur == colors[i + 1]:
                cost.append(neededTime[i + 1])
            else:
                if len(cost) != 1:
                    res += sum(cost) - max(cost)
                cost = [neededTime[i + 1]]
                cur = colors[i + 1]
        if len(cost) != 1:
            res += sum(cost) - max(cost)
        return res
