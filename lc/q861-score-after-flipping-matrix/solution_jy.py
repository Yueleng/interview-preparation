from ast import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # flip row
        for row in grid:
            if row[0] == 0:
                for j in range(n):
                    row[j] = 1 - row[j]

        # flip col
        for j in range(n):
            ones, zeros = 0, 0
            for i in range(m):
                if grid[i][j] == 1:
                    ones += 1
                else:
                    zeros += 1

            if zeros > ones:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        res = 0
        for row in grid:
            num = "".join([str(j) for j in row])
            res += int(num, 2)

        return res
