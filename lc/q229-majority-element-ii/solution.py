from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # init candidate dict which will be value
        # {val1: count1, val2: count2}
        # keep in mind that note the count1, count2 here is not real count
        candidates = {}
        k = 3
        # loop through nums
        for num in nums:
            # add up one count if in candidates
            if num in candidates:
                candidates[num] += 1
            # expand candidates if len < ks
            elif len(candidates) < k:
                candidates[num] = 1
            # if not in candidates and cannot expand any more
            else:
                # try to update candiates
                temp = {}
                for c in candidates:
                    # all candiates with count - 1
                    candidates[c] -= 1
                    # if count == 0, remove that value in candiates
                    # or equivalently, only copy value with count >= 1
                    if candidates[c] >= 1:
                        temp[c] = candidates[c]
                candidates = temp
        out = [k for k in candidates if nums.count(k) > len(nums) // 3]
        return out
