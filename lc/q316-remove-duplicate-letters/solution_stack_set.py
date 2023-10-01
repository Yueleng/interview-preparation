from collections import defaultdict


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dct = defaultdict(int)
        visited = defaultdict(bool)

        # store the rightmost index of character c
        for idx, c in enumerate(s):
            dct[c] = idx

        stck = []

        for idx, c in enumerate(s):
            if visited[c]:
                continue

            # we can safely pop stck[-1] if stck[-1] in later index
            while len(stck) and stck[-1] > c and dct[stck[-1]] > idx:
                visited[stck.pop()] = False

            stck.append(c)
            visited[c] = True

        return "".join(stck)
