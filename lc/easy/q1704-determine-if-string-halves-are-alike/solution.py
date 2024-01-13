class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        # say n = 4, and n // 2 = 2, [0:2] means 0, 1 which is half
        str1 = s[: int(n // 2)]
        str2 = s[int(n // 2) :]
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowel1 = 0
        vowel2 = 0
        for char in str1:
            if char in vowels:
                vowel1 += 1
        for char in str2:
            if char in vowels:
                vowel2 += 1
        return vowel1 == vowel2
