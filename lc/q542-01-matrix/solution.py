from ast import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)

        # rows equal to 0
        if m == 0:
            return []

        # get cols
        n = len(mat[0])

        dis = [[float("inf") for _ in range(n)] for _ in range(m)]

        q = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dis[i][j] = 0
                    q.append((i, j))

        while len(q) > 0:
            x, y = q.pop(0)
            for a, b in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= a < m and 0 <= b < n and dis[a][b] > dis[x][y] + 1:
                    dis[a][b] = dis[x][y] + 1
                    q.append((a, b))

        return dis
