from ast import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def column(_col):
            return [grid[i][_col] for i in range(m)]

        onesRow = [row.count(1) for row in grid]
        onesCol = [column(col).count(1) for col in range(n)]

        zerosRow = [row.count(0) for row in grid]
        zerosCol = [column(col).count(0) for col in range(n)]

        matrix = []

        for i in range(m):
            matrix.append(
                [onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j] for j in range(n)]
            )

        return matrix
