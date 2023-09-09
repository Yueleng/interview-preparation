from ast import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target + 1)

        def get(_target):
            if dp[_target] != -1:
                return dp[_target]
            cum = 0
            for num in nums:
                if num < _target:
                    cum += get(_target - num)
                elif num == _target:
                    cum += 1

            return cum

        for i in range(target + 1):
            dp[i] = get(i)

        print(dp)

        return dp[target]
