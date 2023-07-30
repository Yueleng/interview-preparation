from ast import List
import collections


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        def size_of_distinct(lst):
            temp_dict = collections.defaultdict(int)
            for num in lst:
                temp_dict[num] = 1
            return len(temp_dict)

        min_distinct = size_of_distinct(nums)

        count = 0

        for k in range(min_distinct, n + 1):
            for i in range(0, n - k + 1):
                # window = (i, i + k)
                sub = nums[i : i + k]
                if size_of_distinct(sub) == min_distinct:
                    count += 1

        return count
