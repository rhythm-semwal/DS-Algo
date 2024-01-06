from typing import List


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = []

        for i in range(len(nums)):
            # similar to next greater element, we are maintaining a decreasing order. Whenever that breaks i.e
            # current element is > top of queue than pop elements
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # now if the first element of the queue is out of range i.e > than window than pop that element
            if queue[0] == i - k:
                queue.pop(0)

            # if we have reached the window size then append result
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result


class Solution2:
    # TC = O(k * (n - k))
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = [max(nums[:k])]

        i,j = 1, k
        while j < len(nums):
            answer.append(max(nums[i:j+1]))
            i += 1
            j += 1

        return answer


class Solution3:
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


# A = [1, 3, -1, -3, 5, 3, 6, 7]
# B = 3
# A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
# B = 6
A = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
B = 2
print(Solution().slidingMaximum(A, B))

