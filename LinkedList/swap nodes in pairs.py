# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A is None:
            return None

        dummy_node = ListNode(0)
        dummy_node.next = A
        current = dummy_node

        while current.next is not None and current.next.next is not None:
            first_node = current.next
            second_node = current.next.next

            # this condition is required to maintain the link between all the elements
            first_node.next = second_node.next

            current.next = second_node
            current.next.next = first_node

            current = current.next.next

        return dummy_node.next
