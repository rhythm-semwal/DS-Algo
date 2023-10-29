# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        dummy_node1 = ListNode(0)  # this will have elements < k

        dummy_node2 = ListNode(0)  # this will have elements >= k

        ptr1, ptr2 = dummy_node1, dummy_node2
        current_node = A
        while current_node is not None:
            if current_node.val < B:
                ptr1.next = current_node
                ptr1 = current_node
            else:
                ptr2.next = current_node
                ptr2 = current_node

            # this point is important because there should be no dangling pointers else it will print the same values
            prev = current_node
            current_node = current_node.next
            prev.next = None

        ptr1.next = dummy_node2.next
        return dummy_node1.next
