from ast import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(
            max(left) if len(left) > 0 else 0, n - min(right) if len(right) > 0 else 0
        )
