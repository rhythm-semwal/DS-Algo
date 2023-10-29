# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def removeLoop(self, head, node):
        """
        This method is also dependent on Floyd’s Cycle detection algorithm.
        Detect Loop using Floyd’s Cycle detection algorithm and get the pointer to a loop node.
        Count the number of nodes in loop. Let the count be k.
        Fix one pointer to the head and another to a kth node from the head.
        Move both pointers at the same pace, they will meet at loop starting node.
        Get a pointer to the last node of the loop and make next of it as NULL.
        """
        node1, node2 = node, node
        k = 1

        while node2.next != node1:
            node2 = node2.next
            k += 1

        ptr1, ptr2 = head, head

        while k > 0:
            ptr2 = ptr2.next
            k -= 1

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr2.next != ptr1:
            ptr2 = ptr2.next

        ptr2.next = None

    def solve(self, A):

        if A is None:
            return None

        slow, fast = A, A

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.removeLoop(A, slow)

        return A

        # approach 2 using hash map
        # current = A

        # hash_set = set()
        # hash_set.add(current)
        # while current is not None and current.next not in hash_set:

        #     hash_set.add(current.next)
        #     current = current.next

        # if current:
        #     current.next = None

        # return A
