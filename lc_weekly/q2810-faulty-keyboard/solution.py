class Solution:
    def finalString(self, s: str) -> str:
        def revert(string):
            return string[::-1]

        res = ""
        for char in s:
            if char != "i":
                res += char
            else:
                res = revert(res)
        return res
