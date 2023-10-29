class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        maximum_frequency = 0
        freq_hash_map = dict()
        freq_stack = [[] for _ in range(len(A))]
        result = []
        for i in range(len(A)):
            operation = A[i][0]
            if operation == 1:
                element = A[i][1]
                # add elements in hash map to keep a track of their frequnecy
                if element not in freq_hash_map:
                    freq_hash_map[element] = 1
                    current_freq = 1
                else:
                    current_freq = freq_hash_map[element]+1
                    freq_hash_map[element] = current_freq

                maximum_frequency = max(maximum_frequency, current_freq)
                # add elements in the stack as per their frequencies
                freq_stack[current_freq].append(element)
                result.append(-1)
            else:
                if len(freq_stack[maximum_frequency]) == 0:
                   result.append(-1)
                else:
                    popped_element = freq_stack[maximum_frequency].pop()
                    result.append(popped_element)
                    freq_hash_map[popped_element] -= 1
                    if len(freq_stack[maximum_frequency]) == 0:
                        maximum_frequency -= 1

        print(result)

# A = [       [1, 5],
#             [1, 7],
#             [1, 5],
#             [1, 7],
#             [1, 4],
#             [1, 5],
#             [2, 0],
#             [2, 0],
#             [2, 0],
#             [2, 0] ]
A =  [
        [1, 5],
        [2, 0],
        [1, 4]   ]
Solution().solve(A)