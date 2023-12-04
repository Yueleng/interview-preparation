class Solution:
    def largestGoodInteger(self, num: str) -> str:
        _count = 0
        acc = 0
        cur = ""
        n = len(num)
        good_num = set()
        for i in range(n):
            char = num[i]
            if char != cur:
                acc = 1
                cur = char
            else:
                acc += 1
                if acc >= 3:
                    good_num.add(cur)
        good_num = list(good_num)
        good_num.sort()
        return good_num[-1] * 3 if len(good_num) > 0 else ""
