from ast import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []

        dial_cookbook = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]

        if digits == "":
            return []

        # print(digits)
        def backtrack(remain, perm, nex):
            # solution found
            if remain == 0:
                # print("".join(perm))
                sol.append("".join(perm))

            else:
                # iterate through all possible condidates
                for i in nex:
                    # add character
                    perm.append(i)

                    # backtrack
                    nex_digit = "" if remain == 1 else digits[len(digits) - remain + 1]
                    nex_int = int(nex_digit) if nex_digit != "" else 0
                    backtrack(remain - 1, perm, dial_cookbook[nex_int])

                    # remove candidate
                    perm.pop()

        backtrack(len(digits), [], dial_cookbook[int(digits[0])])

        return sol
