from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []

        def insertable(_arr, _num, _k):
            cnt = 0
            for ele in _arr:
                if abs(ele - _num) <= k:
                    cnt += 1
                if abs(ele - _num) > k:
                    return False
            return cnt != 0

        divided_arr = []
        arr = []
        nums.sort()
        for num in nums:
            if len(arr) == 0:
                arr.append(num)
            elif insertable(arr, num, k):
                arr.append(num)
            else:
                return []
            if len(arr) == 3:
                divided_arr.append(arr)
                arr = []
        return divided_arr
