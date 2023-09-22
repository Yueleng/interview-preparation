from ast import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # problem transformation
        # find interval adds up to target
        target = sum(nums) - x
        acc_sum = 0
        left_idx = 0
        max_count = 0
        flag = 0
        n = len(nums)
        for i in range(n):
            acc_sum += nums[i]

            # window too wide, shink it
            while acc_sum > target:
                acc_sum -= nums[left_idx]
                left_idx += 1

            # window just fit
            if acc_sum == target:
                flag = 1
                max_count = max(max_count, i - left_idx + 1)

        return n - max_count if flag else -1
