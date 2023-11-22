from ast import List
import heapq


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(nums)):
            row = nums[i]
            for j in range(len(row)):
                heapq.heappush(heap, ((i + j, j), row[j]))

        lst = []
        while heap:
            _, num = heapq.heappop(heap)
            lst.append(num)

        return lst
