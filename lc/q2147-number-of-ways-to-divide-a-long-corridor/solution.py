# Combinatorics; Greedy
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        indices = []
        for i, thing in enumerate(corridor):
            if thing == "S":
                indices.append(i)

        # When division is not possible
        if indices == [] or len(indices) % 2 == 1:
            return 0

        # Total number of ways
        count = 1

        # Take the product of non-paired neighbors
        previous_pair_last = 1
        current_pair_first = 2

        while current_pair_first < len(indices):
            count *= indices[current_pair_first] - indices[previous_pair_last]
            count %= MOD
            previous_pair_last += 2
            current_pair_first += 2

        return count
