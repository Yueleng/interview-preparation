from ast import List


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        r = 0
        for i in range(n):
            # purpose of this is to calculate all subarrays starting
            # index at i
            s = set()
            temp = -1
            for j in range(i, n):
                # j is the new element
                if nums[j] not in s:
                    s.add(nums[j])
                    temp += 1 - (nums[j] + 1 in s) - (nums[j] - 1 in s)
                r += temp
        return r
