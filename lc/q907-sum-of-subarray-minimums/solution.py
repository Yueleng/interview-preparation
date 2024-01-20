from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        # left[i] is the index of the first number to the left of arr[i] that is smaller than arr[i]
        # if no such number exists, left[i] is -1
        left = [-1] * n

        # right[i] is the index of the first number to the right of arr[i] that is smaller(or equal) than arr[i]
        # if no such number exists, right[i] is n
        right = [n] * n

        # stack is a monotonic increasing stack of indices
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        mod = 10**9 + 7

        return sum((i - left[i]) * (right[i] - i) * arr[i] for i in range(n)) % mod
