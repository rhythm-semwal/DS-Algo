class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        string_b_hash_map = dict()

        for i in B:
            if i in string_b_hash_map:
                string_b_hash_map[i] += 1
            else:
                string_b_hash_map[i] = 1

        import sys
        left_pointer, right_pointer = -1, -1
        min_length = sys.maxsize

        current_count = 0
        desired_match_count = len(B)
        string_a_hash_map = dict()
        i, j = 0, 0

        while True:
            flag1 = False
            flag2 = False
            # capturing elements
            while i < len(A) and current_count < desired_match_count:
                if A[i] in string_a_hash_map:
                    string_a_hash_map[A[i]] += 1
                else:
                    string_a_hash_map[A[i]] = 1

                if A[i] in string_b_hash_map:
                    if string_a_hash_map[A[i]] <= string_b_hash_map[A[i]]:
                        current_count += 1

                i += 1
                flag1 = True
            # removing elements
            while j < i and current_count == desired_match_count:
                if i-j < min_length:
                    min_length = i-j
                    left_pointer = j
                    right_pointer = i-1

                string_a_hash_map[A[j]] -= 1
                if A[j] in string_b_hash_map:
                    if string_a_hash_map[A[j]] < string_b_hash_map[A[j]]:
                        current_count -= 1
                j += 1
                flag2 = True

            if not flag1 and not flag2:
                break

        print(A[left_pointer:right_pointer+1])

# A = "ADOBECODEBANC"
# B = "ABC"
A = "Aa91b"
B = "ab"
Solution().minWindow(A, B)
