# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        mid_idx = left = 0
        right = mountain_arr.length() - 1

        while left < right:
            mid_idx = (left + right) // 2

            mid_val = mountain_arr.get(mid_idx)
            mid_left = mountain_arr.get(mid_idx - 1)
            mid_right = mountain_arr.get(mid_idx + 1)

            if mid_left < mid_val < mid_right:
                left = mid_idx + 1
            elif mid_left < mid_val and mid_val > mid_right:
                break
            else:
                right = mid_idx

        if left == right:
            mid_idx = left

        def findIndex(target, start, end, asc: bool) -> int:
            def start_should_move_right(target_idx, target):
                if asc:
                    return mountain_arr.get(target_idx) < target
                else:
                    return mountain_arr.get(target_idx) > target

            target_idx = 0

            while start < end:
                target_idx = (start + end) // 2
                if mountain_arr.get(target_idx) == target:
                    return target_idx
                elif start_should_move_right(target_idx, target):
                    start = target_idx + 1
                else:
                    end = target_idx
            if mountain_arr.get(start) == target:
                return start
            return -1

        find_left = findIndex(target, 0, mid_idx, True)

        if find_left != -1:
            return find_left
        else:
            find_right = findIndex(target, mid_idx, mountain_arr.length() - 1, False)
            return find_right

        # found mid idx
        # left , right = 0, mid_idx
        # target_idx = 0
        # while left < right:
        #     target_idx = (left + right) // 2
        #     if mountain_arr.get(target_idx) == target:
        #         return target_idx
        #     elif mountain_arr.get(target_idx) < target:
        #         left = target_idx + 1
        #     else:
        #         right = target_idx

        # if mountain_arr.get(left) == target:
        #     return left

        # # did not found in left
        # left, right = mid_idx, mountain_arr.length() - 1
        # target_idx = 0
        # while left < right:
        #     target_idx = (left + right) // 2
        #     if mountain_arr.get(target_idx) == target:
        #         return target_idx
        #     elif mountain_arr.get(target_idx) > target:
        #         left = target_idx + 1
        #     else:
        #         right = target_idx

        # if mountain_arr.get(left) == target:
        #     return left

        # return -1
