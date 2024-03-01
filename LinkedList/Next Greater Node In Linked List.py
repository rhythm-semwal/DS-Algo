import sys
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to insert node
def insert(root, item):
    temp = ListNode(item)

    if root is None:
        root = temp
    else:
        ptr = root
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = temp

    return root


def display(root):
    while (root != None):
        print(root.val, end="->")
        root = root.next
    print()


def arrayToList(arr, n):
    root = None
    for i in range(0, n, 1):
        root = insert(root, arr[i])

    return root


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        stack = []
        index = 0
        result = []

        while current:
            result.append(0)
            while stack and stack[-1][0] < current.val:
                pop_value, pop_index = stack.pop()
                result[pop_index] = current.val

            stack.append((current.val, index))
            current = current.next
            index += 1

        return result


class Solution1:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next

        result = [0]*len(arr)
        stack = [arr[-1]]
        i = len(arr)-2
        while i >= 0:
            if arr[i] < stack[-1]:
                result[i] = stack[-1]
            else:
                while stack and stack[-1] <= arr[i]:
                    stack.pop()

                if stack:
                   result[i] = stack[-1]

            stack.append(arr[i])
            i -= 1

        return result