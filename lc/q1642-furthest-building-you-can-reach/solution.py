import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        p = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff <= 0:
                continue

            bricks -= diff

            # heap is by default min heap
            # if you want to pop up the maximum, then insert negation of val
            heapq.heappush(p, -diff)

            if bricks < 0:
                bricks += -heapq.heappop(p)
                ladders -= 1

            if ladders < 0:
                return i

        return len(heights) - 1
