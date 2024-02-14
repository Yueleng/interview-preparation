from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        negs = []

        re_arranged = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                negs.append(num)

        for i in range(len(pos)):
            re_arranged.append(pos[i])
            re_arranged.append(negs[i])

        return re_arranged
