from ast import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter


# key point:
#  how to get counter[i] in O(1) time by rely on previous results:
#  counter[0] to counter[i-1]
# bit operation: ``>>``: Bitwise Right Shift Operator
