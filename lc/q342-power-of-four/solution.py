class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        cur = 1

        if n <= 0:
            return False

        while True:
            if cur == n:
                return True
            if n > cur:
                cur *= 4
            else:
                return False
