from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        if left == right:
            return -1 if nums[0] != target else 0

        # Find the index of the pivot element (the smallest element)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:  # nums[mid] <= nums[-1]
                right = mid

        # Binary Search over an inclusive range [left_boundary - right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary

            if left == right:
                return -1 if nums[left] != target else left

            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:  # nums[mid] < target:
                    left = mid + 1

            return -1 if nums[left] != target else left

        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)
