from ast import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)

        # sort to [min, ..., max]
        nums.sort()

        # Find the number of valid parirs by greedy approach
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # if a valid pair is found, skip both numbers
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        # left: thoeretical minimum = 0, right: theoretical maximum = max - min
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            if countValidPairs(mid) < p:
                left = mid + 1
            else:
                right = mid

        return left
