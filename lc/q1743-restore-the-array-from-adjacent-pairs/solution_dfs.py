from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        root = None

        for node in graph:
            if len(graph[node]) == 1:
                root = node
                break

        chain = []

        def dfs(node, prev):
            chain.append(node)
            for neighbour in graph[node]:
                if neighbour != prev:
                    dfs(neighbour, node)

        dfs(root, None)

        return chain
