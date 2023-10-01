class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        words = []
        for c in s:
            if c != " ":
                word.append(c)
            else:
                word.reverse()
                words.append("".join(word))
                word = []

        word.reverse()
        words.append("".join(word))

        return " ".join(words)
