# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        # fast and slow pointer approach
        Time complexity: O(n)O(n)O(n)
        Space complexity: O(1)O(1)O(1)
        """
        
        current = head

        for _ in range(k-1):
            current = current.next
        
        start = current
        end = head

        # when curr reaches the end , second will be at desired node
        while current.next:
            current = current.next
            end = end.next
        
        start.val, end.val = end.val, start.val
        return head
        # print(start.val)
        # print(end.val)
