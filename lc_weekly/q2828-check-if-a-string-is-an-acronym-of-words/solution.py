from ast import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        def _isAcronym(words, s):
            if len(words) == 0:
                return True
            word = words[0]
            if s[0] == word[0]:
                return _isAcronym(words[1:], s[1:])
            return False

        if len(words) != len(s):
            return False

        return _isAcronym(words, s)
