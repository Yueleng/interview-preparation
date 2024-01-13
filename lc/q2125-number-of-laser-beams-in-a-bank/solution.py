from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        if m == 1:
            return 0

        i = 0
        while i <= m - 1:
            row1 = bank[i]
            security_count1 = row1.count("1")
            if security_count1 == 0:
                i += 1
            else:
                break

        beam_count = 0
        for j in range(i + 1, m):
            row2 = bank[j]
            security_count2 = row2.count("1")
            if security_count2 == 0:
                continue

            beam_count += (security_count1) * (security_count2)
            security_count1 = security_count2

        return beam_count
