from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create a graph to represent adjacent pairs
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        # example graph
        # graph = {
        #    1: [1,2],
        #    2: [1,3],
        #    3: [2,4],
        #    4: [3]
        # }

        # Initialize the result array
        chain = []

        # Find the first node that has only one adjacent node
        for node, neighbours in graph.items():
            if len(neighbours) == 1:
                chain.append(node)
                chain.append(neighbours[0])
                break

        # Continue building the array until we reach the end
        while len(chain) < len(adjacentPairs) + 1:
            # get the last two elements in the chain
            last, prev = chain[-1], chain[-2]

            # find the candidates for the next element in the chain
            candidates = graph[last]

            # Choose the candidate
            next_ele = candidates[0] if candidates[0] != prev else candidates[1]

            # Append the candidate to the chain
            chain.append(next_ele)

        return chain
