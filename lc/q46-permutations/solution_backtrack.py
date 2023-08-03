from ast import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def backtrack(remain, perm):
            # solution found
            if remain == 0:
                sol.append(perm.copy())

            else:
                # iterate through all possible candidates
                for i in list(set(nums) - set(perm)):
                    # add candidate
                    perm.append(i)

                    # backtrack
                    backtrack(remain - 1, perm)

                    # remove candidate
                    perm.pop()

        backtrack(len(nums), [])

        return sol
