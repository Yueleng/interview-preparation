from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        cp1 = prices[0] if prices[0] < prices[1] else prices[1]
        cp2 = prices[1] if prices[0] < prices[1] else prices[0]

        for i in range(2, len(prices)):
            if prices[i] < cp1:
                cp2 = cp1
                cp1 = prices[i]
            elif prices[i] >= cp1 and prices[i] < cp2:
                cp2 = prices[i]

        return money - cp1 - cp2 if cp1 + cp2 <= money else money
