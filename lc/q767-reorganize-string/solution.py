from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        # k: key, v: count
        #
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        ans = []

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            ans.extend((x[1], y[1]))

            if x[0] < -1:
                heapq.heappush(heap, (x[0] + 1, x[1]))
            if y[0] < -1:
                heapq.heappush(heap, (y[0] + 1, y[1]))

        if heap:
            if heap[0][0] < -1:
                return ""  # case where last left element count is more than 2
            ans.append(heap[0][1])

        return "".join(ans)
