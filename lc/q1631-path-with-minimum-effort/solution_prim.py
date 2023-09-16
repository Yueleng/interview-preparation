from ast import List
from heapq import heapify, heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        # Prim's MST algorithm
        visited = [[0] * n for _ in range(m)]
        pq, effort = [(0, 0, 0)], 0
        heapify(pq)
        while pq:
            d, to_i, to_j = heappop(pq)
            if visited[m - 1][n - 1]:
                return effort
            if not visited[to_i][to_j]:
                # set this vertex to visited
                visited[to_i][to_j] = 1
                effort = max(effort, d)
                # push possible edges into heap for all the edges connected to vertex
                # [to_i][to_j]
                for r, c in [
                    (to_i - 1, to_j),
                    (to_i + 1, to_j),
                    (to_i, to_j - 1),
                    (to_i, to_j + 1),
                ]:
                    if 0 <= r < m and 0 <= c < n:
                        if not visited[r][c]:
                            heappush(
                                pq,
                                (
                                    abs(heights[r][c] - heights[to_i][to_j]),
                                    r,
                                    c,
                                ),
                            )
        return effort
