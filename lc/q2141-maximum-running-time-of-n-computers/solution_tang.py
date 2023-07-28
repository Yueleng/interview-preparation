class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def helper(val):
            extra = 0
            for i in batteries:
                extra += min(val, i)
            return extra // n >= val

        left, right = 0, sum(batteries) // n
        while left < right:
            mid = math.ceil((left + right) / 2)
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left
