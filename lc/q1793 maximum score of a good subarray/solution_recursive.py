from ast import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def _maximumScore(i, j, _min, cur_max):
            if i == 0 and j == n - 1:
                return cur_max
            moved_idx = 0
            if i == 0:
                j = j + 1
                moved_idx = j
            elif j == n - 1:
                i = i - 1
                moved_idx = i
            elif nums[i - 1] <= nums[j + 1]:
                j = j + 1
                moved_idx = j
            # nums[i] > nums[j]
            else:
                i = i - 1
                moved_idx = i
            _min = min(_min, nums[moved_idx])
            cur_max = max(cur_max, _min * (j - i + 1))
            return _maximumScore(i, j, _min, cur_max)

        return _maximumScore(k, k, nums[k], nums[k])
