class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        cur = 1
        for i in arr:
            if i >= cur:
                cur += 1

        return cur - 1
