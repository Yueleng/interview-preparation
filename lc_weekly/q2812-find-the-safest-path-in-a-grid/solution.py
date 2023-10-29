from ast import List
from collections import defaultdict, deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # nr: # of rows, nc: # of cols
        nr, nc = len(grid), len(grid[0])
        # nxt moves four directions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # store the dist of each pos to (nearest) thieves
        # thus we can expect the dist_to_thief(thief pos) == 0
        dist_to_thief = [[float("inf")] * nc for _ in range(nr)]
        q = deque([])
        # append all thiefs pos(s) into deque q first as starting deque
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    q.append((r, c, 0))

        # record visited pos(s)
        visited = set()
        # tag every other pos(s) with dist, and store the dist (to nearest thieves) with bfs into dist_to_thief (2d array)
        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                dist_to_thief[r][c] = min(dist_to_thief[r][c], dist)

                for r_inc, c_inc in directions:
                    r_next, c_next = r + r_inc, c + c_inc
                    if r_next >= 0 and r_next < nr and c_next >= 0 and c_next < nc:
                        q.append((r_next, c_next, dist + 1))

        _min = float("inf")
        visited = set()
        heap = [(-dist_to_thief[0][0], 0, 0)]

        while heap:
            # pop up heap to get the highest dist
            # (there are some tricks, to negate on purpose is to get the smallest value, but largest in abs value)
            d, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            _min = min(_min, -1 * d)
            # if popped up pos is the right-bottom corner, which means we have get the result
            if r == nr - 1 and c == nc - 1:
                return _min

            visited.add((r, c))
            # append heap with neighbors of current pos
            for r_inc, c_inc in directions:
                r_next, c_next = r + r_inc, c + c_inc
                if r_next >= 0 and r_next < nr and c_next >= 0 or c_next < nc:
                    heapq.heappush(
                        heap, (-dist_to_thief[r_next][c_next], r_next, c_next)
                    )


# from ast import List
# from functools import cache


# class Solution:
#     def canSplitArray(self, nums: List[int], m: int) -> bool:
#         def validSplit(left, right):
#             return (len(left) == 1 or sum(left) >= m) and (
#                 len(right) == 1 or sum(right) >= m
#             )

#         @cache
#         def canSplitSub(start, end):
#             if end - start == 1 or end - start == 2:
#                 return True

#             for i in range(start, end):
#                 left = nums[start:i]
#                 right = nums[i:end]
#                 if not validSplit(left, right):
#                     continue
#                 else:
#                     if canSplitSub(start, i) and canSplitSub(i, end):
#                         return True
#                     else:
#                         continue
#             return False

#         return canSplitSub(0, len(nums))


# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.canSplitArray([2, 3, 3, 2, 3], 6))
