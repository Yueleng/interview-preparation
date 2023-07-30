from ast import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        min_distinct = len(set(nums))

        count = 0
        # max start idx: n - min_distinct
        for i in range(0, n - min_distinct + 1):
            st = set(nums[i : i + min_distinct - 1])
            # j starting point: i + min_distinct
            for j in range(i + min_distinct - 1, n):
                st.add(nums[j])
                if len(st) == min_distinct:
                    count += 1

        return count
