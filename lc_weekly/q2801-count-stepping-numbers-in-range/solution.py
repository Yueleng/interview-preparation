from functools import cache


MOD = int(1e9) + 7


class Solution:
    # count from 0 to n
    def _count(self, n: str) -> int:
        @cache
        def dp(i, tight, lastDigit, leadingZero):
            if i == len(n):
                return 1  # Found a valid number
            maxDigit = int(n[i]) if tight else 9
            ans = 0
            for d in range(maxDigit + 1):
                nxtTight = tight and d == maxDigit
                nxtLeadingZero = leadingZero and d == 0
                if nxtLeadingZero:  # for leading zero, we shouldn't treat lastDigit=d
                    ans = (ans + dp(i + 1, nxtTight, lastDigit, nxtLeadingZero)) % MOD
                elif lastDigit == -1 or abs(lastDigit - d) == 1:
                    ans = (ans + dp(i + 1, nxtTight, d, nxtLeadingZero)) % MOD

            return ans

        return dp(0, True, -1, True)

    def _minusOne(self, s):  # s is a string representing non-negative integer
        num = int(s) - 1
        return str(num)

    def countSteppingNumbers(self, low: str, high: str) -> int:
        if low == "0":
            return self._count(high)
        return (self._count(high) - self._count(self._minusOne(low))) % MOD
