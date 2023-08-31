from ast import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)
        for i in range(n + 1):
            left_i = max(0, i - ranges[i])
            right_i = min(n, i + ranges[i])
            max_reach[left_i] = max(max_reach[left_i], right_i)

        current_right = 0
        next_right = 0
        taps = 0
        for i in range(n + 1):
            if i > next_right:
                return -1
            if i > current_right:
                taps += 1
                current_right = next_right

            # for every i, try to update next_right
            next_right = max(next_right, max_reach[i])
        return taps
