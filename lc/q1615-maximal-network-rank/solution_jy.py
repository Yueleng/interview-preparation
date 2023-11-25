from ast import List
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j in roads:
            d[i].append(j)
            d[j].append(i)
        tmp = [(len(d[i]), i) for i in range(n)]
        pick_max, pick_second_max = [], []
        max_val = 0

        # collect max val(s)
        for i in tmp:
            if i[0] > max_val:
                pick_max = [i]
                max_val = i[0]
            elif i[0] == max_val:
                pick_max.append(i)

        # collect second max val(s)
        second_max_val = 0
        for i in tmp:
            if i[0] == max_val:
                continue
            if i[0] > second_max_val:
                pick_second_max = [i]
                second_max_val = i[0]
            elif i[0] == second_max_val:
                pick_second_max.append(i)

        # if pick_max has length greater than 1
        # solution lies in it, only caveat is to
        # deduct (if possible) 1
        if len(pick_max) > 1:
            for i in range(len(pick_max)):
                for j in range(i + 1, len(pick_max)):
                    if pick_max[j][1] not in d[pick_max[i][1]]:
                        return pick_max[0][0] * 2
            return pick_max[0][0] * 2 - 1
        else:
            # find one from pick_second_max that is not connect
            for i in range(len(pick_max)):
                for j in range(len(pick_second_max)):
                    if pick_second_max[j][1] not in d[pick_max[i][1]]:
                        return pick_max[0][0] + pick_second_max[0][0]
            return pick_max[0][0] + pick_second_max[0][0] - 1
