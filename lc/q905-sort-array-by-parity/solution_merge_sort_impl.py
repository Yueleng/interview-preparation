from ast import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        def compare(num1, num2):
            # num1 is even, then return -1, else 1
            return -1 if num1 % 2 == 0 else 1

        def combine(nums1: List[int], nums2: List[int]) -> List[int]:
            i = 0
            j = 0
            res = []
            # print(nums1)
            # print(nums2)
            while i < len(nums1) and j < len(nums2):
                if compare(nums1[i], nums2[j]) == -1:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1

            if i == len(nums1):
                res.extend(nums2[j:])
            else:
                res.extend(nums1[i:])

            return res

        def _sort(nums):
            if len(nums) == 1:
                return nums
            elif len(nums) == 2:
                return nums if compare(nums[0], nums[1]) == -1 else nums[::-1]

            # len = 5 => half_idx = 2
            # len = 4 => half_idx = 2
            half_idx = len(nums) // 2
            left = _sort(nums[:half_idx])
            right = _sort(nums[half_idx:])
            return combine(left, right)

        return _sort(nums)
