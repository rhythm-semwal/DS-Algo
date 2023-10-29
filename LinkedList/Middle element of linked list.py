# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.data = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        length = 0
        temp = A

        while temp is not None:
            temp = temp.next
            length += 1

        iterations = (length // 2) + 1

        temp = A
        for i in range(iterations - 1):
            # print(temp.data)
            temp = temp.next

        return temp.data

