class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        has_cache = [[[False] * (k + 1) for j in range(m + 1)] for i in range(n + 1)]
        cache = [[[None] * (k + 1) for j in range(m + 1)] for i in range(n + 1)]

        # N: numbers left to fill up the array
        # M: current max number on the left (already filled)
        # K: comparisons left to fill up the array
        def count(N, M, K):
            if N == 0:
                if K == 0:
                    return 1
                return 0

            if has_cache[N][M][K]:
                return cache[N][M][K]

            cnt = 0
            for _ in range(1, M + 1):
                cnt += count(N - 1, M, K)
                cnt %= MOD

            if K > 0:
                for mx in range(M + 1, m + 1):
                    cnt += count(N - 1, mx, K - 1)
                    cnt %= MOD

            has_cache[N][M][K] = True
            cache[N][M][K] = cnt
            return cnt

        return count(n, 0, k)
