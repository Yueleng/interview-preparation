from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # swap A, B to make sure len(A) <= len(B)
        if len(A) > len(B):
            B, A = A, B

        m = len(A)
        n = len(B)
        l, r = 0, m - 1
        half = (m + n) // 2
        # l = 0, r = 4 (m = 5), A_left = 2
        # l = 0, r = 5 (m = 6), A_left = 2

        while True:
            i = (l + r) // 2
            j = half - (i + 1) - 1

            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i + 1] if i + 1 <= m - 1 else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j + 1] if j + 1 <= n - 1 else float("inf")

            if A_left <= B_right and B_left <= A_right:
                if (m + n) % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
