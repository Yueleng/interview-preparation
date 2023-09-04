from ast import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def flip_row(row_num):
            row = grid[row_num]
            for i in range(n):
                row[i] = 1 - row[i]
            grid[row_num] = row

        def column(idx):
            return [row[idx] for row in grid]

        def flip_col(col_num):
            for i in range(m):
                grid[i][col_num] = 1 - grid[i][col_num]

        # flip row
        for i in range(m):
            if grid[i][0] == 0:
                flip_row(i)

        # flip column
        for j in range(n):
            col = column(j)
            # need to flip column
            if 2 * sum(col) < m:
                flip_col(j)

        res = 0
        for row in grid:
            num = "".join([str(j) for j in row])
            res += int(num, 2)

        return res


# greedy:
#   - make sure the row has to be the 1 in the first digit
#   - flip row first and then flip column
# note how the column function is being implemented
# how to quickly convert binary number to decimal? int(num, 2)
