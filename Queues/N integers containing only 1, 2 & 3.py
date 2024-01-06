class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        from collections import deque
        numbers_queue = deque()
        numbers_queue.append(1)
        numbers_queue.append(2)
        numbers_queue.append(3)

        num_count = 3
        result = list()
        # approach 1
        while len(result) < A:
            current = numbers_queue.popleft()
            result.append(current)
            numbers_queue.append(current * 10 + 1)
            numbers_queue.append(current * 10 + 2)
            numbers_queue.append(current * 10 + 3)

        return result

        # approach 2
        # for i in range(num_count, A):
        #     current = numbers_queue[0]
        #     numbers_queue.append(current*10+1)
        #     num_count += 1
        #     numbers_queue.append(current*10+2)
        #     num_count += 1
        #     numbers_queue.append(current*10+3)
        #     num_count += 1

        #     if num_count <= A:
        #         result.append(numbers_queue.popleft())

        # # print(result)
        # # print(numbers_queue)
        # count = len(result)
        # for i in range(count, A):
        #     result.append(numbers_queue.popleft())
        # return result
