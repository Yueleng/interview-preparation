#
# Complete the 'cacheContents' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_INTEGER_ARRAY calllogs as parameter.
#
from collections import defaultdict


def cacheContents(calllogs):
    # sort the calllogs by timestamp
    calllogs.sort(key=lambda x: x[0])

    cache = defaultdict(int)

    current_time = 0
    for time, item in calllogs:

        time_passed = time - current_time
        current_time = time

        for key, (priority, flag) in cache.items():
            if time_passed > 0:
                if priority > time_passed:
                    # decrement the time passed from the value
                    priority -= time_passed
                    if key == item:
                        priority += 1

                    # move out of memory
                    if priority <= 3:
                        flag = False

                    cache[key] = (priority, flag)

                elif priority == time_passed:
                    if key == item:
                        priority = 1
                    else:
                        priority = 0
                    # move out of Cache
                    flag = False
                    cache[key] = (priority, flag)

                # priority < time_passed
                else:
                    # remove the key from the cache
                    # del cache[key]
                    # remove from cache violates the cache is being modified while iterating
                    # so we just set the flag to False
                    cache[key] = (0, False)

        # add the item to the cache
        (priority, flag) = cache.get(item, (0, False))
        priority += 2
        if priority > 5:
            flag = True
        cache[item] = (priority, flag)

    # return the keys of the cache
    return [k for k, v in cache.items() if v[1]]


print(cacheContents([[1, 1], [2, 1], [2, 1], [4, 2], [5, 2], [6, 2]]))
print(cacheContents([[1, 1], [2, 1], [2, 1], [4, 2], [5, 2], [6, 2], [7, 1]]))
print(cacheContents([[1, 1], [2, 1], [2, 1], [4, 2], [5, 2], [6, 2], [7, 1], [8, 1]]))
print(
    cacheContents(
        [[1, 1], [2, 1], [2, 1], [4, 2], [5, 2], [6, 2], [7, 1], [8, 1], [10, 3]]
    )
)

#           1    2     3
# day 1:    2    0
# day 2     6    0
# day 3     5    0
# day 4     4    2
# day 5     3    4
# day 6     2    6
# day 7     4    5
# day 8     6    4
# day 9     5    3
# day 10    4    2     2
