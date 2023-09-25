class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        excess = [[0 for _ in range(100)] for _ in range(100)]
        # store = [[0 for for j in range(100)] for i in range(100)]
        excess[0][0] = poured - 1 if poured >= 1 else 0
        # store[0][0] = if poured >= 1 else poured
        for i in range(1, 100):
            for j in range(i + 1):
                upper_left = (i - 1, j - 1)
                upper_right = (i - 1, j)

                sum = 0
                if (
                    upper_left[0] >= 0
                    and upper_left[1] >= 0
                    and excess[upper_left[0]][upper_left[1]] > 0
                ):
                    sum += excess[upper_left[0]][upper_left[1]] / 2
                if (
                    upper_right[0] >= 0
                    and upper_right[1] >= 0
                    and excess[upper_right[0]][upper_right[1]] > 0
                ):
                    sum += excess[upper_right[0]][upper_right[1]] / 2

                # store[i][j] = 1 if sum >= 1 else sum
                excess[i][j] = sum - 1
        excess_row_glass = (
            (
                excess[query_row - 1][query_glass - 1] / 2
                if query_row - 1 >= 0
                and query_glass - 1 >= 0
                and excess[query_row - 1][query_glass - 1] >= 0
                else 0
            )
            + (
                excess[query_row - 1][query_glass] / 2
                if query_row - 1 >= 0
                and query_glass >= 0
                and excess[query_row - 1][query_glass] >= 0
                else 0
            )
            if query_row >= 1
            else poured
        )

        return 1 if excess_row_glass >= 1 else excess_row_glass
