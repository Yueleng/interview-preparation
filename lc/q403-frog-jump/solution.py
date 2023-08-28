from ast import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {}
        for i in stones:
            dp[i] = set()

        # initial analysis
        dp[0].add(1)
        if 1 in dp:
            dp[1].add(1)
            dp[1].add(2)
        else:
            return False

        # loop start from idx 1
        for i in range(1, len(stones)):
            stone_val = stones[i]
            if len(dp[stone_val]):
                for step_len in dp[stone_val]:
                    next_stone = stone_val + step_len
                    if next_stone in dp:
                        dp[next_stone].add(step_len)
                        dp[next_stone].add(step_len + 1)
                        if step_len > 1:
                            dp[next_stone].add(step_len - 1)

        return len(dp[stones[i]]) > 0
