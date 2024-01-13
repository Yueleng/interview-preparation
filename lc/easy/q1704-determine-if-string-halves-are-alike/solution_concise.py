class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = s[: int(len(s) / 2)].lower()

        r = s[int(len(s) / 2) :].lower()

        vovel = ["a", "e", "i", "o", "u"]
        cnt_l = 0
        cnt_r = 0
        for i in vovel:
            if i in l:
                cnt_l += l.count(i)

            if i in r:
                cnt_r += r.count(i)

        return cnt_l == cnt_r
