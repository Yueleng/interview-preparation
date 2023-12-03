from ast import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0

        def diff(p1: List[int], p2: List[int]) -> int:
            diff_x = abs(p1[0] - p2[0])
            diff_y = abs(p1[1] - p2[1])
            return max(diff_x, diff_y)

        _sum = 0
        for i in range(n - 1):
            p1 = points[i]
            p2 = points[i + 1]
            _sum += diff(p1, p2)

        return _sum
