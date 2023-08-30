from ast import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        # Start from the second last element, as the las one is always sorted.
        for i in range(n - 2, -1, -1):
            # No need to break if they are already in order.
            if nums[i] <= nums[i + 1]:
                continue

            #
            # num_elements = (nums[i] + nums[i+1] - 1) // nums[i+1]

            num_elements = (
                (nums[i] // nums[i + 1])
                if nums[i] % nums[i + 1] == 0
                else nums[i] // nums[i + 1] + 1
            )

            #
            ans += num_elements - 1

            nums[i] = nums[i] // num_elements

        return ans
