from typing import List
from functools import cmp_to_key


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        def compare(item1, item2):
            return item1[0] - item2[0]

        _points = sorted(points, key=cmp_to_key(compare))

        _gap = -1
        for i in range(1, len(_points)):
            _gap = max(_gap, _points[i][0] - _points[i - 1][0])

        return _gap
