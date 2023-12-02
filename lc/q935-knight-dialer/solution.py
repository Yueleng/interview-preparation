from functools import cache


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def next_of(i: int, remain: int) -> int:
            if remain == 0:
                return 1
            else:
                match i:
                    case 1:
                        return (next_of(6, remain - 1) + next_of(8, remain - 1)) % MOD
                    case 2:
                        return (next_of(7, remain - 1) + next_of(9, remain - 1)) % MOD
                    case 3:
                        return (next_of(8, remain - 1) + next_of(4, remain - 1)) % MOD
                    case 4:
                        return (next_of(0, remain - 1) + next_of(3, remain - 1) + next_of(9, remain - 1)) % MOD
                    case 5:
                        return 0
                    case 6:
                        return (next_of(0, remain - 1) + next_of(1, remain - 1) + next_of(7, remain - 1)) % MOD
                    case 7:
                        return (next_of(2, remain - 1) + next_of(6, remain - 1)) % MOD
                    case 8:
                        return (next_of(1, remain - 1) + next_of(3, remain - 1)) % MOD
                    case 9:
                        return (next_of(2, remain - 1) + next_of(4, remain - 1)) % MOD
                    case 0:
                        return (next_of(4, remain - 1) + next_of(6, remain - 1)) % MOD
            
        sum = 0
        for i in range(10):
            sum = (sum + next_of(i, n - 1)) % MOD
        
        return sum
        
