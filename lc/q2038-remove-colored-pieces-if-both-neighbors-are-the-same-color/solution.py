class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a = 0
        count_b = 0
        current_a = 0
        current_b = 0
        for color in colors:
            if color == "A":
                current_a += 1
                current_b = 0
                if current_a >= 3:
                    count_a += 1

            elif color == "B":
                current_b += 1
                current_a = 0
                if current_b >= 3:
                    count_b += 1

        return count_a > count_b
