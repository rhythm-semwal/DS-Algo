# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        if A is None:
            return 0

        slow, fast = A, A
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        reverse_list = slow
        prev = None

        while reverse_list is not None:
            next = reverse_list.next
            reverse_list.next = prev
            prev = reverse_list
            reverse_list = next

        node1, node2 = A, prev

        while node2 is not None:
            if node1.val != node2.val:
                return 0
            else:
                node1 = node1.next
                node2 = node2.next
        return 1