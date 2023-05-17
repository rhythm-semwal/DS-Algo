# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Logic = Reverse the second half of the LL.
        Find the middle element of the LL
        Reverse the LL from the middle to the end
        Then compare the start and middle element and find the max sum by incrementing both the start and middle

        TC = O(N)
        SC = O(1)
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        max_sum = 0
        start = head
        while prev:
            max_sum = max(max_sum, start.val + prev.val)
            prev = prev.next
            start = start.next
        return max_sum

    def pairSum1(self, head: Optional[ListNode]) -> int:
        """
              TC = O(N)
              SC = O(N)
        """
        arr = []

        current = head

        while current is not None:
            arr.append(current.val)
            current = current.next
        
        start, end = 0, len(arr)-1

        result = 0
        while start < end:
            result = max(result, arr[start] + arr[end])
            start += 1
            end -= 1
        
        return result

        
