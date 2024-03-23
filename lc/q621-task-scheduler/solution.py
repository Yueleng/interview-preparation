import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # RC
        # Approach: HashMap
        # Logic: Take the maximum frequency element and make those many number of Slots
        # Slot size: (n+1) if n = 2 => slotsize = 3
        # Example: {A:5, B:1} => ABxAxxAxxAxxAxx
        # indices of A = 0,2 and middle there should be n elements, so slot size should be n+1

        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #

        # freq = [6, 4, 2]
        freq = collections.Counter(tasks).values()

        # maxFreq = 6
        maxFreq = max(freq)

        # maxFreqCount = 1
        maxFreqCount = list(freq).count(maxFreq)

        # ans = (6 - 1) * 3 + 1
        ans = (maxFreq - 1) * (n + 1) + maxFreqCount

        return max(ans, len(tasks))
