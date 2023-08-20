class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = set(range(1, n + 1))

        for i in range(1, n + 1):
            # i in res: because res could already have removed i in previous loop
            # i < k: if i >= k, there is no way that i + j == k
            # k - i != i, because we need two distinct i and j such that i + j == k
            # (k -i) in res, means we need to avoid k - i
            if i in res and i < k and k - i != i and (k - i) in res:
                res.remove(k - i)
                res.add(n + i)

        return sum(res)
