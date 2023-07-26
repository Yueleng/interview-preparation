from ast import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1

        # left, right = 1, max(dist), hour - math.floor(hour) != 0 ? dist[-1] / (hour - math.floor(hour))
        def moveToLeft(dist, spd):
            total = 0
            for i in dist[:-1]:
                total += math.ceil(i / spd)
            total += dist[-1] / spd
            return total <= hour

        def isInt(num):
            return num - math.floor(num) == 0

        def decPart(num):
            return math.modf(num)[0]

        left, right = 1, max(dist) if isInt(hour) else max(
            max(dist), dist[-1] / decPart(hour)
        )

        while left < right:
            mid = (left + right) // 2
            if moveToLeft(dist, mid):
                right = mid
            else:
                left = mid + 1
        return int(left)
