from ast import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        count, cum = 0, 0
        for num in nums:
            cum += num
            remain = cum % k
            count += mp[remain]
            mp[remain] += 1
        return count

    # mp defaultdict(<class 'int'>, {0: 1})

    # loop 0
    # num 4
    # cum 4
    # remain 4
    # count 0
    # update mp to defaultdict(<class 'int'>, {0: 1, 4: 1})

    # loop 1
    # num 5
    # cum 9
    # remain 4
    # count 1
    # update mp to defaultdict(<class 'int'>, {0: 1, 4: 2})

    # loop2
    # num 0
    # cum 9
    # remain 4
    # count  3 (1 + 2)
    # update mp to defaultdict(<class 'int'>, {0: 1, 4: 3})

    # loop3
    # num -2
    # cum 7
    # remain 2
    # count 3 (1 + 2)
    # update mp to defaultdict(<class 'int'>, {0: 1, 4: 3, 2: 1})

    # loop4
    # num -3
    # cum 4
    # remain 4
    # count 6 (1 + 2 + 3)
    # update mp to defaultdict(<class 'int'>, {0: 1, 4: 4, 2: 1})

    # loop5
    # num 1
    # cum 5
    # remain 0
    # count 7 (1 + 2 + 3 + 1)
    # update map to defaultdict(<class 'int'>, {0: 2, 4: 4, 2: 1})
