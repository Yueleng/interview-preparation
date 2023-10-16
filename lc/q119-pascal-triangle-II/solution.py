from ast import List
import math


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []

        def n_chooses_i(n, i):
            i = n - i if i > n - i else i
            val = 1
            for j in range(i):
                val *= n - j
            return int(val / math.factorial(i))

        for i in range(rowIndex + 1):
            res.append(n_chooses_i(rowIndex, i))
        return res
