from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        sets = []
        for num in nums:
            flag = False  # False means not taken care
            for _set in sets:
                if num not in _set:
                    _set.add(num)
                    flag = True  # True means taken care
                    break

            if not flag:
                new_set = set()
                new_set.add(num)
                sets.append(new_set)

        matrix = []
        for _set in sets:
            matrix.append(list(_set))

        return matrix
