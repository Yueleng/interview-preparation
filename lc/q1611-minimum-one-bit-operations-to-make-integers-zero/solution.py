class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        flag = True
        while n:
            intermediate = ((-1) if flag else 1) * (n ^ (n - 1))

            res += intermediate

            n &= n - 1
            flag = not flag

        return abs(res)
