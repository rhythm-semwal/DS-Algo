# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, n: int):
        current = head
        ll_len = 0

        while current:
            ll_len += 1
            current = current.next

        if ll_len == n:
            return head.next

        node = head
        for _ in range(ll_len - n - 1):
            node = node.next

        node.next = node.next.next
        return head

    def removeNthFromEnd1(self, A, B):
        if A.next is None and B == 1:
            A = None
            return A

        length = 0
        temp = A
        while temp is not None:
            temp = temp.next
            length += 1

        if length <= B:
            temp = A
            A = temp.next
            return A

        temp = A
        for i in range(length - B - 1):
            temp = temp.next

        temp.next = temp.next.next

        return A
