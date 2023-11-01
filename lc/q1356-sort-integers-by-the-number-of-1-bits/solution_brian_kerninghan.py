from ast import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Brian Kerninghan's Algorithm
        def countBits(num):
            count = 0

            while num > 0:
                count += 1
                num &= num - 1  # Clear the least significant set bit.

            return count

        return sorted(arr, key=lambda num: (countBits(num), num))
