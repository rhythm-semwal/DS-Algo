# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A is None:
            return None

        slow, fast = A, A
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        current_node = slow
        prev = None

        while current_node is not None:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next

        node1, node2 = A, prev

        # node2.next condition is imp else it goes into an infinite loop
        while node2.next is not None:
            temp1 = node1.next
            temp2 = node2.next

            node1.next = node2
            node2.next = temp1

            node1 = temp1
            node2 = temp2

        return A
