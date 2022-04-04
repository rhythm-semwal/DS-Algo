# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    # approach 1 = most optimal one
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    # approach 2
    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length = 0

        while current is not None:
            length += 1
            current = current.next

        current = head
        count = length//2
        while count > 0:
            current = current.next
            count -= 1

        return current

