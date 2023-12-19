from math import floor
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        def calculate_avg(i, j):
            denom = 0
            sum = 0
            # left-upper-corner
            if i >= 1 and j >= 1:
                sum += img[i - 1][j - 1]
                denom += 1

            # upper-cell
            if i >= 1:
                sum += img[i - 1][j]
                denom += 1

            # upper-right cell
            if i >= 1 and j <= n - 2:
                sum += img[i - 1][j + 1]
                denom += 1

            # left cell
            if j >= 1:
                sum += img[i][j - 1]
                denom += 1

            # itself
            sum += img[i][j]
            denom += 1

            # right cell
            if j <= n - 2:
                sum += img[i][j + 1]
                denom += 1

            # left-buttom cell
            if i <= m - 2 and j >= 1:
                sum += img[i + 1][j - 1]
                denom += 1

            # bottom cell
            if i <= m - 2:
                sum += img[i + 1][j]
                denom += 1

            # bottom right cell
            if i <= m - 2 and j <= n - 2:
                sum += img[i + 1][j + 1]
                denom += 1

            return floor(sum / denom)

        result = []

        for i in range(m):
            result.append([])
            for j in range(n):
                center = (i, j)
                result[i].append(calculate_avg(i, j))

        return result
