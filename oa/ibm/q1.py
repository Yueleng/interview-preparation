# Write a function that returns the maximum mex of a given array.
# Mex is the minimum non-negative integer that is not in the array.
# Any array value can be reduced to any number >= 0
# for exmaple arr = [1, 2, 3, 5] can be reduced to [0, 1, 2, 3]
# thus the mex of arr is 4


def getMaximumMex(arr):
    arr.sort()
    mex = 1
    for i in range(len(arr)):
        if arr[i] <= mex:
            mex += arr[i]
        else:
            break
    return mex
