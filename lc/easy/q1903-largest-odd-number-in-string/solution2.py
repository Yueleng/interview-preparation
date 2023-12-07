class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num[
            : max(
                num.rfind("1"),
                num.rfind("3"),
                num.rfind("5"),
                num.rfind("7"),
                num.rfind("9"),
            )
            + 1
        ]
