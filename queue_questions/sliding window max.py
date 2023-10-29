class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        # approach 1
        from collections import deque
        queue = deque()
        ans = list()
        # front, rear = 0, -1
        n = len(A)
        for i in range(n):

            # this loop is for sliding the window when front element index is > than the window
            while queue and queue[0] <= i-B:
                queue.popleft()

            # this loop is for removing the elements from the back if the current rear element is < A[i]
            # this maintains a descending order in the queue
            while queue and A[queue[-1]] < A[i]:
                queue.pop()

            queue.append(i)

            # if i exceed the window size add it to the ans

            if i >= B-1:
                ans.append(A[queue[0]])

        return ans

        # approach 2
        # queue = list() # store indexes
        # # ans array will be of len(A)-B+1
        # ans = list()
        # front, rear = 0, -1
        # n = len(A)
        # for i in range(n):
        #
        #     # this loop is for sliding the window when front element index is > than the window
        #     while queue and queue[front] <= i-B:
        #         queue.pop(front)
        #         rear -= 1
        #
        #     # this loop is for removing the elements from the back if the current rear element is < A[i]
        #     # this maintains a descending order in the queue
        #     while queue and A[queue[rear]] < A[i]:
        #         queue.pop(rear)
        #         rear += 1
        #
        #     queue.append(i)
        #     rear += 1
        #
        #     # if i exceed the window size add it to the ans
        #
        #     if i >= B-1:
        #         ans.append(A[queue[front]])
        #
        # return ans



# A = [1, 3, -1, -3, 5, 3, 6, 7]
# B = 3
# A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
# B = 6
A = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
B = 2
print(Solution().slidingMaximum(A, B))

