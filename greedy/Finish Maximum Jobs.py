from functools import cmp_to_key
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    @staticmethod
    def letter_cmp(a, b):
        if a[1] > b[1]:
            return 1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            else:
                return -1
        else:
            return -1

    def solve(self, A, B):
        compare_key = cmp_to_key(self.letter_cmp)
        start_end_time_zipped_array = list(zip(A, B))

        start_end_time_zipped_array.sort(key=compare_key)
        # print(start_end_time_zipped_array)

        count = 1
        current_start_time = start_end_time_zipped_array[0][0]
        current_end_time = start_end_time_zipped_array[0][1]
        for i in range(1, len(start_end_time_zipped_array)):
            if start_end_time_zipped_array[i][0] < current_end_time:
                continue
            else:
                count += 1
                current_end_time = start_end_time_zipped_array[i][1]

        return count

    def solve(self, A, B):

        letter_cmp_key = cmp_to_key(self.letter_cmp)
        zipped_array = list(zip(A, B))

        zipped_array.sort(key=letter_cmp_key)
        # print(zipped_array)
        jobs = 1
        result = 1
        i, j = 1, 0
        n = len(A)
        while i < n and j < n:

            if zipped_array[j][1] > zipped_array[i][0]:
                i += 1
            else:
                jobs += 1
                # j += 1
                j = i
                i += 1
                result = max(result, jobs)

        return result