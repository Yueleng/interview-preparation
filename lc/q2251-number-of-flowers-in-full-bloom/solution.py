from ast import List
from bisect import bisect_left, bisect_right


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        # start = [1, 3, 4, 9]
        start = sorted(a for a, b in flowers)

        # end = [6, 7, 12, 13]
        end = sorted(b for a, b in flowers)

        # for people: [2, 3, 7, 11]
        # bisect_right(start, 2) - bisect_left(end, 2) = 1 - 0 = 1
        # bisect_right(start, 3) - bisect_left(end, 3) = 2 - 0 = 2
        # bisect_right(start, 7) - bisect_left(end, 7) = 3 - 1 = 2
        # bisect_right(start, 11) - bisect_left(end, 11) = 4 - 2 = 2
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]
