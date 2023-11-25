from ast import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        flag = [False]
        wordSet = set(wordDict)

        def backtrack(remain):
            if flag[0]:
                return
            if len(remain) == 0:
                flag[0] = True
                return

            else:
                # iterate through all possible candidates
                for i in range(len(remain)):
                    if flag[0]:
                        return
                    candidate = remain[: i + 1]
                    if candidate in wordSet:
                        print(candidate)
                        backtrack(remain[i + 1 :])

        backtrack(s)

        return flag[0]
