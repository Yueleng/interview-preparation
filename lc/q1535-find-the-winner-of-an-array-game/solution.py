from ast import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        i = j = 0
        while True:
            if arr[i] > arr[j + 1]:
                j += 1
            else:
                i = j + 1
                j += 1

            if i == 0 and j - i == k:
                return arr[0]

            if i > 0 and j - i == k - 1:
                return arr[i]

            if j == len(arr) - 1:
                return arr[i]
