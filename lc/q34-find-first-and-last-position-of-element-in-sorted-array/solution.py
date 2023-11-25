from ast import List
from math import ceil


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        start_p = 0
        end_p = 0

        range_left = 0
        range_right = n - 1

        while True:
            mid = (range_left + range_right) // 2
            # target = 10, array = [1,2,3,4,5,6,7,8,8,10]
            # print(range_left, range_right, mid)
            # print(len(nums))
            if nums[mid] < target:
                range_left = mid + 1
            # nums[mid] >= target
            else:
                range_right = mid

            if range_left >= range_right:
                start_p = range_right if nums[range_right] == target else -1
                # print("about to break")
                break

        range_left = 0
        range_right = n - 1

        while True:
            mid = ceil((range_left + range_right) / 2)
            if nums[mid] > target:
                range_right = mid - 1
            # nums[mid] <= target
            else:
                range_left = mid
            # print(range_left, range_right, mid)
            if range_right <= range_left:
                # print("about to break")
                end_p = range_left if nums[range_left] == target else -1
                break

        return [start_p, end_p]
