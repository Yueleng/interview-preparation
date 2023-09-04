from ast import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        # keep records of all indices that up to ith index,
        # count of nums[j] % modulo == k for j from 0 to i(includisve)
        prefix = [0 for _ in range(n)]
        for i in range(n):
            prefix[i] = (prefix[i - 1] if i > 0 else 0) + (nums[i] % modulo == k)
        count = defaultdict(int)
        ans = 0
        count[0] = 1
        for i in range(n):
            j = prefix[i] - k
            remain = j % modulo
            ans += count[remain]
            count[prefix[i] % modulo] += 1
        return ans


# Subarray sums divisible by modulo and remains k
# prefix = [a_0, a_1, ..., a_n]
# we want all subarrays prefix[i:j] s.t.
# sum(a[i:j]) % modulo == k
# so if we have F[i], then we need to find an F[j]
# where j < i, s.t.
#   1. (F[i] - F[j]) % modulo = k
#   2. (F[i] - k) % modulo = F[j] % modulo
# F[i] calculate as you go through the array
# F[j] stored in hashmap
