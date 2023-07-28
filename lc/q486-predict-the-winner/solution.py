from ast import List
import collections


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = collections.defaultdict(int)

        def maxDiff(left, right):
            if left == right:
                return nums[left]

            tmp1 = nums[left] - maxDiff(left + 1, right)
            tmp2 = nums[right] - maxDiff(left, right - 1)
            memo[(left, right)] = max(tmp1, tmp2)
            return memo[(left, right)]

        return maxDiff(0, n - 1) >= 0
