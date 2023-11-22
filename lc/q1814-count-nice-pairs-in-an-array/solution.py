from ast import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(num: int) -> int:
            rev = 0
            while num > 0:
                rev = rev * 10 + num % 10
                num //= 10
            return rev

        mod = 1000000007
        nums = [num - reverse(num) for num in nums]

        nums.sort()

        res = 0
        i = 0

        while i < len(nums) - 1:
            count = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                count += 1
                i += 1
            res = (res % mod + (count * (count - 1)) // 2) % mod
            i += 1

        return res % mod
