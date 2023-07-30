class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s1, s2):
            if s2 in s1:
                return s1

            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i] + s2

            return s1 + s2

        res, l = "", len(a + b + c) + 1
        for s in [
            merge(merge(a, b), c),
            merge(merge(b, a), c),
            merge(merge(c, b), a),
            merge(merge(b, c), a),
            merge(merge(a, c), b),
            merge(merge(c, a), b),
        ]:
            if len(s) < l:
                res, l = s, len(s)
            elif len(s) == l:
                res = min(res, s)

        return res
