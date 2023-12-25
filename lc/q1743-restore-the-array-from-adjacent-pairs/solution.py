from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        _map = defaultdict(list)
        for i in range(n - 1):
            _map[adjacentPairs[i][0]].append(sorted(adjacentPairs[i]))
            _map[adjacentPairs[i][1]].append(sorted(adjacentPairs[i]))

        # example _map
        # map = {
        #    1: [[1,2]],
        #    2: [[1,2], [2,3]],
        #    3: [[2,3], [3,4]],
        #    4: [[3,4]]
        # }

        _pointer = -1
        for key in _map:
            if len(_map[key]) == 1:
                _pointer = key
                break

        chain = [_pointer]
        [remove] = _map.pop(key)
        _pointer = remove[1] if remove[0] == _pointer else remove[0]
        chain.append(_pointer)
        while _map:
            list_of_array = _map.pop(_pointer)

            # determine if only returns only one array
            if len(list_of_array) == 1:
                # chain.append(_pointer)
                break

            [array1, array2] = list_of_array

            # array1 equals remove
            array2 = array2 if array1 == remove else array1

            # update pointer
            _pointer = array2[0] if array2[0] != _pointer else array2[1]

            # append to chain in this loop
            chain.append(_pointer)

            remove = array2

        return chain
