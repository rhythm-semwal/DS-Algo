class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


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
        while (ptr.next != None):
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


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    # arr = [1]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)