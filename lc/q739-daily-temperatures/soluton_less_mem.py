from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n

        for idx, temp in enumerate(temperatures):
            # current new temp, large,
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                ele_idx = stack.pop()
                answer[ele_idx] = idx - ele_idx
            stack.append(idx)

        return answer
