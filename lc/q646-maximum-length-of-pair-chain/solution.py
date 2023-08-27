from ast import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort by last
        pairs.sort(key=lambda x: x[1])
        last_second = float("-inf")
        res = []
        for first, second in pairs:
            if first > last_second:
                res.append([first, second])
                last_second = second
        return len(res)
