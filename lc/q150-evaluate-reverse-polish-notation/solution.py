from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []

        operations = ["+", "-", "*", "/"]

        def _eval(left_num, right_num, _operand):
            if _operand == "+":
                return left_num + right_num
            elif _operand == "-":
                return left_num - right_num
            elif _operand == "*":
                return left_num * right_num
            else:
                return int(left_num / right_num)

        for token in tokens:
            if token in operations:
                right = int(stack.pop())
                left = int(stack.pop())
                temp = _eval(left, right, token)
                stack.append(temp)
            else:
                stack.append(token)

        return stack[-1]
