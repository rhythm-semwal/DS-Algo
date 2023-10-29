class Tree:
    def __init__(self, x):
        self.val = x
        self.smaller = 0
        self.left = None
        self.right = None

# Time Complexity: O(nLogn)
# Auxiliary Space: O(n)
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        smaller = [0 for _ in range(n)]

        if n < 2:
            return smaller

        root = Tree(A[-1])

        for i in range(n-2, -1, -1):
            node = root
            count = 0

            while True:
                # this will keep a track of smaller elements apart from the root
                if A[i] < node.val:
                    print("node.val = ", node.val)
                    print("node.smaller = ", node.smaller)
                    node.smaller += 1

                    if not node.left:
                        node.left = Tree(A[i])
                        break
                    else:
                        node = node.left
                else:
                    # in case A[i] > root and in between A[i] and root there are certain values less than root and
                    # > than A[i], then node.smaller will have that count
                    count += node.smaller
                    # this check is with the root node of RST
                    if A[i] > node.val:
                        count += 1
                    if not node.right:
                        node.right = Tree(A[i])
                        break
                    else:
                        node = node.right

            smaller[i] = count

        print(smaller)


A = [3,4,5,1,2]
Solution().solve(A)
