from ast import List
from collections import defaultdict
from heapq import heapify, heappop


class Weighted_UF:
    def __init__(self, n: int):
        self.ids = list(range(n))
        self.weights = [0] * n

    def union(self, p: int, q: int):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:
            return

        if self.weights[parent_p] > self.weights[parent_q]:
            parent_p, parent_q = parent_q, parent_p

        self.ids[parent_p] = parent_q
        self.weights[parent_q] += self.weights[parent_p]

    def find(self, p: int) -> int:
        while p != self.ids[p]:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        # collect edges
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                edges.append((d, i, j))
        heapify(edges)
        uf, total_weight, connected_edge_cnt = Weighted_UF(n), 0, 0
        while connected_edge_cnt != n - 1:
            weight, root, child = heappop(edges)
            if not uf.connected(root, child):
                uf.union(root, child)
                connected_edge_cnt += 1
                total_weight += weight

        return total_weight
