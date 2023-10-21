from ast import List
from collections import defaultdict

#  Write a function:
#  def solution(A, B)
#  that, given two arrays A and B of N integers each, describing a directed graph
#  return True if the graph has a cycle and False otherwise


def checkCycle(A: [int], B: [int]) -> bool:
    n = len(A)

    # Defining visited and inStack array
    # to keep track of visited vertices
    # and vertices in Recursive stack
    # assume worst case that edge + 1 = nodes
    visited = [False] * (n + 1)
    inStack = [False] * (n + 1)

    # defining adjacency list to represent graph
    graph = [[] for _ in range(max(max(A), max(B)) + 1)]

    def addEdge(_graph, u, v):
        _graph[u].append(v)

    # build graph
    for i in range(len(A)):
        addEdge(graph, A[i], B[i])

    def checkCycleUtil(node, visited, inStack):
        # Check if node exists in the
        # recursive stack
        if inStack[node]:
            return True

        # Check if node is already visited
        if visited[node] == True:
            return False

        # marking node as visited
        visited[node] = True

        # marking node to be present in
        # recursive stack
        inStack[node] = True

        for v in graph[node]:
            if checkCycleUtil(v, visited, inStack) == True:
                return True

        # Mark 'node' to be removed
        # from the recursive stack
        inStack[node] = False

        # Return false if no cycle exists
        return False

    for node, neighbors in enumerate(graph):
        if len(neighbors) > 0:
            if checkCycleUtil(node, visited, inStack) == True:
                return True

    return False


if __name__ == "__main__":
    assert True == checkCycle([3, 1, 2], [2, 3, 1])

    assert False == checkCycle([1, 2, 1], [2, 3, 3])

    assert True == checkCycle([1, 2], [2, 2])
