# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
      """
      TC = O(N)
      SC = O(N)
      """
        arr = []

        current = head

        while current is not None:
            arr.append(current.val)
            current = current.next
        
        start, end = 0, len(arr)-1

        result = 0
        while start < end:
            result = max(result, arr[start] + arr[end])
            start += 1
            end -= 1
        
        return result

        
