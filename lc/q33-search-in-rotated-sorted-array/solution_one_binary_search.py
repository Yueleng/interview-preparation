from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if left == right:
            return -1 if nums[0] != target else 0

        while left < right:
            mid = (left + right) // 2

            # Case 1: find target
            if nums[mid] == target:
                return mid

            # Case 2: subarray on mid's left is sorted
            elif nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            # Case 3: subarray on mid's right is sorted
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid

        return -1 if nums[left] != target else left
