class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        # Start from the second last element, as the las one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue

            # num_elements = (nums[i] + nums[i+1] - 1) // nums[i+1]

            # if num[i] is divisible by nums[i+1]
            # break the nums[i] into (nums[i] / nums[i+1]) part
            # else break the nums[i] into (nums[i] // nums[i+1] + 1) part

            divisible = nums[i] % nums[i + 1] == 0

            num_elements = (
                (nums[i] // nums[i + 1]) if divisible else nums[i] // nums[i + 1] + 1
            )

            ans += num_elements - 1

            # get the maximum that nums[i] could be
            nums[i] = nums[i] // num_elements

        return ans
