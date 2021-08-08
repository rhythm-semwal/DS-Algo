# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list\
    def merge(self, node1, node2):
        sorted_list = ListNode(0)
        current = sorted_list

        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next

            current = current.next

        if node1 is not None:
            current.next = node1
        if node2 is not None:
            current.next = node2

        return sorted_list.next

    def mergeSort(self, A):
        # base case
        if A is None or A.next is None:
            return A
        # find mid point
        slow, fast = A, A

        while fast is not None and fast.next is not None:
            # temp variable will track the tail of the left side of the node will be 1 step behind the slow node
            temp = slow
            slow = slow.next
            fast = fast.next.next

        temp.next = None  # this is the left side node
        # right side node will be from slow to fast

        left_side_node = self.mergeSort(A)
        right_side_node = self.mergeSort(slow)

        return self.merge(left_side_node, right_side_node)

    def sortList(self, A):
        if A is None or A.next is None:
            return A

        return self.mergeSort(A)
