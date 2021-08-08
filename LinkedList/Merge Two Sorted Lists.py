# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        prev = dummy = ListNode(None)

        while A and B:
            if A.val < B.val:
                prev.next = A
                A = A.next
            else:
                prev.next = B
                B = B.next

            prev = prev.next

        prev.next = A or B
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A is None:
            return B
        if B is None:
            return A
        # A node will point to always the smaller element
        # B node will point to always the greater element
        if A.val > B.val:
            temp = A
            A = B
            B = temp

        result = A
        while A is not None and B is not None:
            # this will maintain the previous state of A
            temp = None
            while A is not None and A.val <= B.val:
                temp = A
                A = A.next

            # for correcting the link point temp i.e previous state of A to B which is smaller than A
            temp.next = B

            # swapping the values
            temp = A
            A = B
            B = temp

        return result
