class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n

        while left < right:
            target = right - (right - left) // 2

            extra = 0
            for power in batteries:
                extra += min(power, target)

            if extra // n < target:
                right = target - 1
            else:
                left = target

        return right
