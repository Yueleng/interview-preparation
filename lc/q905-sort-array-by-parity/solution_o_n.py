from ast import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd_array = []
        even_array = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_array.append(nums[i])
            else:
                odd_array.append(nums[i])

        return even_array + odd_array
