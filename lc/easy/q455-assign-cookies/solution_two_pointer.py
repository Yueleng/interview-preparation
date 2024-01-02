from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        content = 0
        n = len(g)
        m = len(s)
        i, j = 0, 0
        while i <= n - 1 and j <= m - 1:
            # fit
            if g[i] <= s[j]:
                content += 1
                i += 1
                j += 1
            else:
                # g[i] > s[j], not fit
                j += 1
        return content
