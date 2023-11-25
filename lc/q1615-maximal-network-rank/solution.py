from ast import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # graph as adjacency list
        graph = {}

        for u, v in roads:
            graph.setdefault(u, set()).add(v)
            graph.setdefault(v, set()).add(u)

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                val = (
                    len(graph.get(i, set()))
                    + len(graph.get(j, set()))
                    - (j in graph.get(i, set()))
                )
                ans = max(ans, val)

        return ans
