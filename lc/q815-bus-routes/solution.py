from ast import List
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # map m records <stop, set(bus_idx)> relationship
        m = defaultdict(set)
        for i, route in enumerate(routes):
            for node in route:
                # m[node] means how many buses passes node
                m[node].add(i)

        ans = -1
        vis = set()
        queue = deque()
        queue.append(source)
        while queue:
            ans += 1
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if node == target:
                    return ans
                for bus in m[node]:
                    if not bus in vis:
                        vis.add(bus)
                        queue.extend(routes[bus])

        return -1
