from ast import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def column(matrix, i):
            return [row[i] for row in matrix]

        m = len(mat)
        n = len(mat[0])

        count = 0
        for i in range(m):
            if sum(mat[i]) == 1:
                i = mat[i].index(1)
                col = column(mat, i)
                if sum(col) == 1:
                    count += 1
        return count
