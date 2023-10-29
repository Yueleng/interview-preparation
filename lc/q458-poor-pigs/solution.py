# Explanation and Solution

# With 2 pigs, poison killing in 15 minutes, and having 60 minutes, we can find the poison in up
# to 25 buckets in the following way. Arrange the buckets in a 5 X 5 square:

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# Now use one pig to find the row (make it drink from buckets 1, 2, 3, 4, 5 wait 15 minutes,
# make it drink from buckets 6,7,8,9,10 wait 15 minutes, etc). Use the second pig to find the column
# (make it drink 1, 6, 11, 16, 21, then 2, 7, 12, 17, 22, etc)

# Having 60 minutes and tests taking 15 minutes means we can run four tests. If the row pig dies in the third test, the
# poison is the third row. If the column pig doesn't die at all, the poison is the fifth column (this is why we can cover five
# rows/columns even though we can only run four tests).

# With 3 pigs, we can similarly use a 5 X 5 X 5 cube instead of 5 X 5 square and again use one pig to determine the coordinate
# of one dimension (one pig drinks layers from top to bottom, one drink layers from left to right, one drinks layers from front to back)
# So 3 pigs can solve up to 125 buckets.

# In general, we can solve up to (math.floor(minutesToTest / minutesToDie) + 1)^(pigs) buckets this way, so just
# find the smallest number of pigs for example like this:


class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        max_bucket_one_time_one_pig = minutesToTest / minutesToDie + 1
        while max_bucket_one_time_one_pig**pigs < buckets:
            pigs += 1
        return pigs
