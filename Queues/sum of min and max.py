class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        1) First window size K
  1.1) For deque 'G', if current element is greater
       than rear end element, we remove rear while
       current is greater.
  1.2) For deque 'S', if current element is smaller
       than rear end element, we just pop it while
       current is smaller.
  1.3) insert current element in both deque 'G' 'S'

2) After step 1, front of 'G' contains maximum element
   of first window and front of 'S' contains minimum
   element of first window. Remaining elements of G
   and S may store maximum/minimum for subsequent
   windows.

3) After that we do traversal for rest array elements.
  3.1) Front element of deque 'G' is greatest and 'S'
       is smallest element of previous window
  3.2) Remove all elements which are out of this
       window [remove element at front of queue ]
  3.3) Repeat steps 1.1 , 1.2 ,1.3

4) Return sum of minimum and maximum element of all
   sub-array size k.
        """
        from collections import deque
        min_queue = deque()
        max_queue = deque()
        n = len(A)

        for i in range(B):

            while len(max_queue) > 0 and A[max_queue[-1]] <= A[i]:
                max_queue.pop()

            while len(min_queue) > 0 and A[min_queue[-1]] >= A[i]:
                min_queue.pop()

            min_queue.append(i)
            max_queue.append(i)

        result = 0
        for i in range(B, n):
            result += A[min_queue[0]] + A[max_queue[0]]

            while len(min_queue) > 0 and min_queue[0] <= i - B:
                min_queue.popleft()
            while len(max_queue) > 0 and max_queue[0] <= i - B:
                max_queue.popleft()

            while len(max_queue) > 0 and A[max_queue[-1]] <= A[i]:
                max_queue.pop()

            while len(min_queue) > 0 and A[min_queue[-1]] >= A[i]:
                min_queue.pop()

            min_queue.append(i)
            max_queue.append(i)

        result += A[min_queue[0]] + A[max_queue[0]]
        return result % 1000000007

