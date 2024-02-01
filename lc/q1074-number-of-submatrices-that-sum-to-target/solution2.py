from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # m: # of rows
        # n: # of cols
        m, n = len(matrix), len(matrix[0])

        for col in range(n):
            # stack every row's val into next row
            for row in range(1, m):
                matrix[row][col] += matrix[row - 1][col]

        count = 0

        # first two for loops are to get the start and end of the rows of submatrix
        # r1: start of row, r2: end of row
        for r1 in range(m):
            for r2 in range(r1, m):
                prefix_sum_count = {0: 1}
                sum_val = 0

                # third for loop is to get the start and end of the cols of submatrix
                for col in range(n):
                    # rhs: sum of curr_col from r1 to r2 (inclusive)
                    # lhs: sum from col0 to curr_col from r1 to r2 (inclusive)
                    sum_val += matrix[r2][col] - (matrix[r1 - 1][col] if r1 > 0 else 0)

                    # trick step: current sum = target + prev_sum
                    count += prefix_sum_count.get(sum_val - target, 0)

                    # store the count of current sum
                    prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1

        return count
