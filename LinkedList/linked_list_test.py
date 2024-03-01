import random
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
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.list = self.make_list(self.head)

    def make_list(self, head):
        current = head
        result = []

        while current:
            result.append(current)
            current = current.next

        return result

    def getRandom(self) -> int:
        print(random.choice(self.list).val)



if __name__ == "__main__":
    arr = [2,7,4,3,5]
    # arr = [3, 3]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)

    obj = Solution(root)
    param_1 = obj.getRandom()
