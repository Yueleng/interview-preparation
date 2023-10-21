from ast import List
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # Initialize a deque to track max sum in a window of size k
        dq = deque()
        # loop through each number in nums
        for i in range(len(nums)):
            # Add max sum from last k positions or 0 if deque is empty
            nums[i] += nums[dq[0]] if dq else 0

            # Ensure deque is in decreasing order and within window size
            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()

            # Append positive numbers to the deque
            if nums[i] > 0:
                dq.append(i)

        # Return the max value from modified nums
        return max(nums)
