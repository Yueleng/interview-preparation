from ast import List
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adjacencyList = [[] for _ in range(n)]

        for edge in edges:
            self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    def addEdge(self, edge: List[int]) -> None:
        self.adjacencyList[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)

    # Dijkstra's algorithm path between two nodes using Dijkstra's algorithm
    def dijkstra(self, start: int, end: int) -> int:
        # num of nodes
        n = len(self.adjacencyList)

        # init distances to infinity
        distances = [float("inf")] * n

        distances[start] = 0

        priorityQueue = [(0, start)]

        while priorityQueue:
            currentCost, currentNode = heapq.heappop(priorityQueue)

            # Skip if a shorter path has already been found
            if currentCost > distances[currentNode]:
                continue

            # If found the target node then return the cost
            if currentNode == end:
                return currentCost

            for edge in self.adjacencyList[currentNode]:
                neighbor, edgeLength = edge
                newRouteCost = edgeLength + distances[currentNode]

                # Update distance if a shorter route is found
                if distances[neighbor] > newRouteCost:
                    distances[neighbor] = newRouteCost
                    heapq.heappush(priorityQueue, (newRouteCost, neighbor))

        return -1 if distances[end] == float("inf") else distances[end]


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
