from ast import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] = 1 - row[j]
