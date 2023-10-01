class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        countList = [0] * 26
        boolList = [False] * 26
        stack = []

        for char in s:
            countList[ord(char) - ord("a")] += 1

        for char in s:
            countList[ord(char) - ord("a")] -= 1
            if boolList[ord(char) - ord("a")]:
                continue

            while (
                stack and char < stack[-1] and countList[ord(stack[-1]) - ord("a")] > 0
            ):
                boolList[ord(stack[-1]) - ord("a")] = False
                stack.pop()

            stack.append(char)

            boolList[ord(char) - ord("a")] = True

        return "".join(stack)
