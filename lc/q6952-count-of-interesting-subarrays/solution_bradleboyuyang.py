from ast import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (nums[i] % modulo == k)
        count = defaultdict(int)
        ans = 0
        for i in range(n + 1):
            j = prefix[i] - k
            ans += count[j % modulo]
            count[prefix[i] % modulo] += 1
        return ans
