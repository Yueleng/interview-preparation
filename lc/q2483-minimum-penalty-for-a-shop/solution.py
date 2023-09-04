class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_index = 0
        current_penalty = 0
        best_penalty = 0
        n = len(customers)
        for i in range(n):
            if customers[i] == "Y":
                current_penalty -= 1
            elif customers[i] == "N":
                current_penalty += 1

            if current_penalty < best_penalty:
                best_index = i + 1
                best_penalty = current_penalty
        return best_index


# algorithm: how to define a proper current_penalty variable
#  for a new time: if customer then deduct, if empty then increase
