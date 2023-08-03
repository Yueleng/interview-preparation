from ast import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, s):
            if i == len(nums):
                res.append(s)
                return
            for c in nums:
                if c in s:
                    continue
                dfs(i + 1, s + [c])

        dfs(0, [])
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, s):
            if i == len(nums):
                res.append(s)
                return
            for c in list(set(nums) - set(s)):
                dfs(i + 1, s + [c])

        dfs(0, [])
        return res
