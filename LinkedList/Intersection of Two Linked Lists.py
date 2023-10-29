# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Method 1(Simply use two loops) 
Use 2 nested for loops. The outer loop will be for each node of the 1st list and inner loop will be for 2nd list. 
In the inner loop, check if any of nodes of the 2nd list is same as the current node of the first linked list. 
The time complexity of this method will be O(M * N) where m and n are the numbers of nodes in two lists
"""

"""
Method 2 (Use Hashing) 
Basically, we need to find a common node of two linked lists. So we hash all nodes of the first list and then check the second list. 
1) Create an empty hash set. 
2) Traverse the first linked list and insert all nodes’ addresses in the hash set. 
3) Traverse the second list. For every node check if it is present in the hash set. If we find a node in the hash set, return the node.
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_set = set()

        A = headA

        while A is not None:
            hash_set.add(A)
            A = A.next

        B = headB
        while B is not None:
            if B in hash_set:
                return B
            B = B.next

        return B


"""
Method 3( 2-pointer technique ): Best approach
1. Initialize two pointers ptr1 and ptr2  at the head1 and  head2.
2. Traverse through the lists,one node at a time.
3. When ptr1 reaches the end of a list, then redirect it to the head2.
4. similarly when ptr2 reaches the end of a list, redirect it the head1.
5. Once both of them go through reassigning,hey will be equidistant from
 the collision point
6. If at any node ptr1 meets ptr2, then it is the intersection node.
7. After second iteration if there is no intersection node it returns NULL.
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        A = headA
        B = headB

        while A != B:
            if A is None:
                A = headB
            else:
                A = A.next

            if B is None:
                B = headA
            else:
                B = B.next
        return A