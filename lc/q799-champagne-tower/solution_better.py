class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[-1 for _ in range(query_row + 1)] for query_row in range(100)]
        # print(dp)

        dp[0][0] = poured

        def cal_champagne_poured(row, col):
            if col < 0:
                return 0
            if row < 0:
                return 0
            if col > row:
                return 0
            if dp[row][col] >= 0:
                return dp[row][col]
            upper_left_poured = (
                (cal_champagne_poured(row - 1, col - 1) - 1) / 2
                if cal_champagne_poured(row - 1, col - 1) >= 1
                else 0
            )
            upper_poured = (
                (cal_champagne_poured(row - 1, col) - 1) / 2
                if cal_champagne_poured(row - 1, col) >= 1
                else 0
            )
            acc_poured = upper_left_poured + upper_poured
            dp[row][col] = acc_poured
            return acc_poured

        return (
            1
            if cal_champagne_poured(query_row, query_glass) >= 1
            else cal_champagne_poured(query_row, query_glass)
        )
