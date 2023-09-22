from ast import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # problem transformation
        # find interval adds up to target
        target = sum(nums) - x
        acc_sum = 0
        left_idx = 0
        for i in range(len(nums)):
            acc_sum += nums[i]

            # window too wide, shink it
            if acc_sum > target:
                acc_sum -= nums[left_idx]
                left_idx += 1
