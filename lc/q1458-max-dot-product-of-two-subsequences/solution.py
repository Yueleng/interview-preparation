from ast import List
from functools import cache


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def max_prod_from(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            temp = nums1[i] * nums2[j]
            _max = max(
                temp + max_prod_from(i + 1, j + 1)
                if temp > 0
                else max_prod_from(i + 1, j + 1),
                max_prod_from(i, j + 1),
                max_prod_from(i + 1, j),
            )

            return _max

        if all(i < 0 for i in nums1) and all(j > 0 for j in nums2):
            return max(nums1) * min(nums2)
        if all(i > 0 for i in nums1) and all(j < 0 for j in nums2):
            return min(nums1) * max(nums2)

        return max_prod_from(0, 0)
