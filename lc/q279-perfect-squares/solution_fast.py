# does not quite get this

import math


class Solution:
    def numSquares(self, n: int) -> int:
        sq = int(math.sqrt(n))
        if sq * sq == n:
            return 1

        ans = [10**4 for _ in range(n + 1)]

        ans[1] = 1

        for i in range(2, n + 1):
            # sq: the maximum square root of i
            sq = int(math.sqrt(i))
            if sq**2 == i:
                ans[i] = 1

            else:
                x = sq

                # why lower bound is sq // 2?
                # because if x < sq // 2, say sq = 6, x = 2, then squre = x**2 = 4
                # then i - square = 37 - 4 = 33, then what???
                while x >= sq // 2:
                    square = x**2
                    count = ans[i - square] + 1
                    ans[i] = min(ans[i], count)
                    x -= 1

        return ans[-1]
