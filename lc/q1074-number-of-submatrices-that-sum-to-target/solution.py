from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # m: # of rows
        # n: # of cols
        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            # stack every col's val into next col
            for col in range(1, n):
                matrix[row][col] += matrix[row][col - 1]

        count = 0
        # first two for loops are to get the start and end of the cols of submatrix
        # c1: start of col, c2: end of col
        for c1 in range(n):
            for c2 in range(c1, n):
                prefix_sum_count = {0: 1}
                sum_val = 0

                # third for loop is to get the start and end of the rows of submatrix
                for row in range(m):
                    # rhs: sum of curr_row from c1 to c2 (inclusive)
                    # lhs: sum from row0 to curr_row from c1 to c2 (inclusive)
                    sum_val += matrix[row][c2] - (matrix[row][c1 - 1] if c1 > 0 else 0)

                    # trick step: current sum = target + prev_sum
                    count += prefix_sum_count.get(sum_val - target, 0)

                    # store the count of current sum
                    prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1

        return count
