class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_diff = abs(fx - sx)
        y_diff = abs(fy - sy)
        _min = max(x_diff, y_diff)

        if _min == 0:
            return False if t == 1 else True

        return t >= _min
