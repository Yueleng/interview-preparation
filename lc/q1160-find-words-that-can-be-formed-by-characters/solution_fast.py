from ast import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        for word in words:
            for char in word:
                if word.count(char) > chars.count(char):
                    break
            else:
                result += len(word)
        return result
