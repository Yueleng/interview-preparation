from ast import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # create a list to track the maximum reach for each position
        max_reach = [0] * (n + 1)

        # calculate the maximum reach for each tap
        for i in range(n + 1):
            # calculate the leftmost position the tap can reach
            left_i = max(0, i - ranges[i])
            # calculate the rightmost position the tap can reach
            right_i = min(n, i + ranges[i])
            # update the maximum reach(value: right position) for the leftmost position
            # i.e. max[1] = 10,  means there is an interval [1, 10]
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
            # important: this make sure that we have the furthest next_right
            # when chosing next_right
            next_right = max(next_right, max_reach[i])
        return taps
