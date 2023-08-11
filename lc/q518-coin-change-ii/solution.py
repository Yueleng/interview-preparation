from ast import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # memo[i][j] = number of ways to make up amount j using coins[:i]
        # dimension: len(coins) * (amount + 1)
        memo = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        def numberOfWays(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            elif i == len(coins):
                return 0

            # cache hit
            if memo[i][amount] != -1:
                return memo[i][amount]

            # cache miss
            if coins[i] > amount:
                # must skip current coin
                memo[i][amount] = numberOfWays(i + 1, amount)
            else:
                # use current coin or skip current coin
                memo[i][amount] = numberOfWays(i, amount - coins[i]) + numberOfWays(
                    i + 1, amount
                )

            return memo[i][amount]

        return numberOfWays(0, amount)
