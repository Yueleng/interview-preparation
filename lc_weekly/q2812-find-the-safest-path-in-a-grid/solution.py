from collections import defaultdict, deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # nr: # of rows, nc: # of cols
        nr, nc = len(grid), len(grid[0])
        # nxt moves four directions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # represent with dict for ??
        adj_list = defaultdict(list)
        # store the dist of each pos to (nearest) thieves
        board = [[float("inf")] * nc for _ in range(nr)]
        q = deque([])
        # append all thiefs pos(s) into deque q
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    q.append((r, c, 0))

        # record visited pos(s)
        visited = set()
        # tag every other pos(s) with dist, and store the dist (to nearest thieves) with bfs into board (2d array)
        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                if r < 0 or r >= nr or c < 0 or c >= nc:
                    continue
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                board[r][c] = min(board[r][c], dist)

                for r_inc, c_inc in directions:
                    r_next, c_next = r + r_inc, c + c_inc
                    q.append((r_next, c_next, dist + 1))

        output = float("inf")
        visited = set()
        heap = [(-board[0][0], 0, 0)]

        while heap:
            d, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            output = min(output, -1 * d)
            if r == nr - 1 and c == nc - 1:
                return output

            visited.add((r, c))
            for r_inc, c_inc in directions:
                r_next, c_next = r + r_inc, c + c_inc
                if r_next < 0 or r_next >= nr or c_next < 0 or c_next >= nc:
                    continue
                heapq.heappush(heap, (-board[r_next][c_next], r_next, c_next))


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
