import collections


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitute_table = collections.defaultdict(lambda: -1)

        order = 0
        for char in key:
            if char == " ":
                continue
            # char not in dict
            if substitute_table[char] == -1:
                substitute_table[char] = order
                order += 1

        decipher = ""
        for m in message:
            deciphered_m = ""
            if m != " ":
                deciphered_m = chr(substitute_table[m] + ord("a"))
            else:
                deciphered_m = " "
            decipher += deciphered_m

        return decipher
