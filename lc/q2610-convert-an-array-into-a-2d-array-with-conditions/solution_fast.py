from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # {num: array_position}
        # keep the info that last num's position
        kl = {}
        matrix = [[]]
        for num in nums:
            if num not in kl:
                # if num never appeared before
                # coz new num will be put into the first array
                kl[num] = 0
            else:
                # if num appeared before
                kl[num] += 1
                if kl[num] > len(matrix) - 1:
                    matrix.append([])

            matrix[kl[num]].append(num)
        return matrix
