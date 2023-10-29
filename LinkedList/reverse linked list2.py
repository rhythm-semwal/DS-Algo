# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        prev = None
        current_node = A

        while B > 1:
            prev = current_node
            current_node = current_node.next
            B -= 1
            C -= 1

        left_side = prev
        right_side = current_node

        while C > 0:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
            C -= 1

        if left_side is not None:
            left_side.next = prev
        else:
            A = prev

        right_side.next = current_node

        return A
