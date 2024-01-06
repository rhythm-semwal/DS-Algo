class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = ""
        hash_set = dict()

        queue = list()

        for i in range(len(A)):
            if A[i] not in hash_set:
                hash_set[A[i]] = 1
                queue.append(A[i])
            else:
                hash_set[A[i]] += 1

            if not queue:
                ans += '#'

            elif hash_set[queue[0]] == 1:
                ans += queue[0]

            else:
                while queue and hash_set[queue[0]] != 1:
                    queue.pop(0)

                if queue:
                    ans += queue[0]
                else:
                    ans += '#'

        return ans
# class Solution:
#     # @param A : string
#     # @return a strings
#     def solve(self, A):
#         # approach 1
#         n = len(A)
#         my_queue = list()
#         hash_map = dict()
#         front, rear = 0, -1
#         result = ""
#         for i in range(n):
#             if A[i] not in hash_map:
#                 hash_map[A[i]] = 1
#             else:
#                 hash_map[A[i]] += 1
#
#             if hash_map[A[i]] == 1:
#                 # add to my_queue
#                 # check overflow condition
#                 if rear - front == n - 1:
#                     return
#                 else:
#                     rear += 1
#                     my_queue.append(A[i])
#
#             while len(my_queue) > 0 and hash_map[my_queue[front]] != 1:
#                 my_queue.pop(front)
#
#             if len(my_queue) == 0:
#                 result += '#'
#             else:
#                 result += my_queue[front]
#
#         return result
#
#         # approach 2
#         # n = len(A)
#         # my_queue = list()
#         # hash_map = dict()
#         # front, rear = 0, -1
#         # result = ""
#         # for i in range(n):
#         #     if A[i] not in hash_map:
#         #         hash_map[A[i]] = 1
#         #     else:
#         #         hash_map[A[i]] += 1
#         #
#         #     if hash_map[A[i]] == 1:
#         #         # add to my_queue
#         #         # check overflow condition
#         #         if rear-front == n-1:
#         #             return
#         #         else:
#         #             rear += 1
#         #             my_queue.append(A[i])
#         #             # my_queue[rear] = A[i]
#         #
#         #     while len(my_queue) > 0:
#         #         # while my_queue[front] != 0:
#         #         print(my_queue[front])
#         #         if hash_map[my_queue[front]] == 1:
#         #             result += my_queue[front]
#         #             break
#         #         else:
#         #             my_queue.pop(front)
#         #             # my_queue[front] = 0
#         #             front += 1
#         #
#         #     if my_queue[front] == 0:
#         #         result += '#'
#         #
#         # print(result)
#
# # A = "abadbc"
# A = "cegdwewvuxbtgbdwkkvxvguscqknlupskunrbwvomiikklu"
A = "abcabc"
print(Solution().solve(A))
#
#
