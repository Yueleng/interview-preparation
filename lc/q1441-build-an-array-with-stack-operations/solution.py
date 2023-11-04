from ast import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        oprs = []
        cur_pointer = 1
        for i in target:
            if i == cur_pointer:
                oprs.append("Push")
                cur_pointer += 1
            else:
                while cur_pointer < i:
                    oprs.append("Push")
                    oprs.append("Pop")
                    cur_pointer += 1
                oprs.append("Push")
                cur_pointer += 1
        return oprs
