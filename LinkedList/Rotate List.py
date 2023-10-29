# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None or k == 0:
            return head

        current = head
        length = 1

        # calculate the length
        while current.next is not None:
            length += 1
            current = current.next

        if k == length:
            return head

        # Currently current pointer points to the last node. So point the last node to head.
        current.next = head

        k = k % length
        # steps to be taken from tail node to reach node whose next is to be made NULL
        to_move = length - k

        while to_move > 0:
            current = current.next
            to_move -= 1

        head = current.next
        current.next = None

        return head
