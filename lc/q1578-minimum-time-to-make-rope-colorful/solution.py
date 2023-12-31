from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        cost = 0
        cur_color = colors[0]
        length = len(colors)
        start = 0
        end = 0

        for i in range(1, length):
            color = colors[i]
            if color == cur_color:
                # move end index to next
                end += 1

            else:
                # reassign cur_color
                cur_color = color

                # calculate cost
                _slice = neededTime[start : end + 1]
                cost += sum(_slice) - max(_slice)

                start = end = i

        # calculate cost
        _slice = neededTime[start : end + 1]
        _slice.sort()
        cost += sum(_slice) - max(_slice)

        return cost
