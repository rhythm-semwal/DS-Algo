# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        # approach 1
        if A is None:
            return None

        current = A

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return A

        # in case list is not sorted
        # hash_set = set()
        # if A.next is None:
        #     return A
        # temp = A
        # hash_set.add(temp.val)
        # while temp.next is not None:
        #     if temp.next.val not in hash_set:
        #         hash_set.add(temp.next.val)
        #         temp = temp.next
        #     else:
        #         if temp.next.next is None:
        #             temp.next = None
        #         else:
        #             temp.next = temp.next.next
        # return A

