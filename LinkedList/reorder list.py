# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

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

        node1, node2 = head, prev

        while node2.next is not None:
            node1_next = node1.next
            node2_next = node2.next

            node1.next = node2
            node2.next = node1_next

            node1 = node1_next
            node2 = node2_next

        return head
