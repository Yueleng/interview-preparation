class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = 0
        suffix_sum = sum(nums)
        ans = [0] * n

        for i, x in enumerate(nums):
            ans[i] = (x * i - prefix_sum) + (suffix_sum - x * (n - i))
            prefix_sum += x
            suffix_sum -= x

        return ans
