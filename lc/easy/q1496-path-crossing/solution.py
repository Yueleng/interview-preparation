class Solution:
    def isPathCrossing(self, path: str) -> bool:
        _map = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        if len(path) == 0:
            return True
        visited = set()
        visited.add((0, 0))
        loc = _map[path[0]]
        visited.add(loc)

        for i in range(1, len(path)):
            loc = (loc[0] + _map[path[i]][0], loc[1] + _map[path[i]][1])
            if loc in visited:
                return True

            visited.add(loc)

        return False
