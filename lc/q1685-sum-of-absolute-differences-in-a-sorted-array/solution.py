from ast import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        suffix_sum = sum(nums) - nums[0]
        n = len(nums)
        result = []
        result.append(suffix_sum - nums[0] * (n - 1))
        for i in range(1, n):
            prefix_sum += nums[i - 1]
            suffix_sum -= nums[i]
            result.append(
                (nums[i] * i - prefix_sum) + (suffix_sum - nums[i] * (n - 1 - i))
            )

        return result
