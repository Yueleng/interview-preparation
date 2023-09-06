from ast import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        def get_length(lst):
            count = 0
            head1 = lst
            while head1:
                count += 1
                head1 = head1.next
            return count

        def get_arr_len(n, k):
            base = n // k
            arr = [base] * k
            remain = n % k
            for i in range(remain):
                arr[i] += 1
            print(n, k, arr)
            return arr

        def split_into_k(lst, arr):
            parts = []
            cur = lst
            for i in range(len(arr)):
                part = cur
                # length of each part arr[i]
                # important
                for _ in range(arr[i] - 1):
                    cur = cur.next
                if cur:
                    temp = cur.next
                    cur.next = None
                    cur = temp
                parts.append(part)
            return parts

        n = get_length(head)
        arr = get_arr_len(n, k)

        return split_into_k(head, arr)
