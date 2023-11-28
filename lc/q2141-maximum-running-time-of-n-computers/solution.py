# Time Exceeded
from ast import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def swap(lst, i, j):
            lst[i], lst[j] = lst[j], lst[i]

        def insertSort(lst, itr):
            left = itr
            while left > 0:
                for i in range(left, len(lst)):
                    if lst[i - 1] > lst[i]:
                        swap(lst, i - 1, i)
                        continue
                    # lst[i-1] <= lst[i], current itration finished
                    break
                left -= 1

        def oneMinUse(lst, n, cum):
            for i in range(len(lst) - n, len(lst)):
                lst[i] -= 1
            return cum + 1

        nonZeroIdx = 0
        time = 0
        # len(lst) == 5, and n = 3, then nonZeroIdx = 2, it's fine
        # but nonZeroIdx = 3
        while nonZeroIdx <= len(batteries) - n:
            time += oneMinUse(batteries, n, time)
            # len(lst) == 5, n = 3, nonZeroIdx = 0, then need 2 iterations
            insertSort(batteries, len(batteries) - nonZeroIdx)
            for i in range(nonZeroIdx, len(batteries)):
                if batteries[i] > 0:
                    continue
                nonZeroIdx = i
                break
        return time
