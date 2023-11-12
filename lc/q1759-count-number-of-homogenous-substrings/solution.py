from collections import defaultdict


class Solution:
    def countHomogenous(self, s: str) -> int:
        module = 1000000007
        dct = defaultdict(int)
        dct[s[0]] = 1
        cur = s[0]
        acc = 1
        _sum = 1

        for i in range(1, len(s)):
            if s[i] == cur:
                acc += 1
                _sum += acc
                # for j in range(1, acc + 1):
                #     dct[cur * j] += 1
            else:
                acc = 1
                cur = s[i]
                _sum += 1

        return _sum % module
