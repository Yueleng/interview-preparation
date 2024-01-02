from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = 0
        si = 0
        for si in range(len(s)):
            if gi >= len(g):
                return gi

            # gi <= len(g) - 1
            if g[gi] <= s[si]:
                gi += 1

        return gi
