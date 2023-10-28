from functools import cache


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # top down dp

        @cache
        def start_with(_char, cnt):
            if cnt == 1:
                return 1
            if _char == "a":
                return start_with("e", cnt - 1) % 1000000007
            if _char == "e":
                return (
                    start_with("a", cnt - 1) + start_with("i", cnt - 1)
                ) % 1000000007
            if _char == "i":
                return (
                    start_with("a", cnt - 1)
                    + start_with("e", cnt - 1)
                    + start_with("o", cnt - 1)
                    + start_with("u", cnt - 1)
                ) % 1000000007
            if _char == "o":
                return (
                    start_with("i", cnt - 1) + start_with("u", cnt - 1)
                ) % 1000000007
            if _char == "u":
                return (start_with("a", cnt - 1)) % 1000000007

        return (
            start_with("a", n)
            + start_with("e", n)
            + start_with("i", n)
            + start_with("o", n)
            + start_with("u", n)
        ) % 1000000007
