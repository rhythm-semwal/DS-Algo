class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        if A == 1:
            return 11
        if A == 2:
            return 22
        perfect_number_array = list()
        perfect_number_array.append('11')
        perfect_number_array.append('22')

        current_count = 2
        while current_count < A:
            temp_array = list()
            for i in range(len(perfect_number_array)):
                temp_array.append('1'+perfect_number_array[i]+'1')

            for i in range(len(perfect_number_array)):
                temp_array.append('2' + perfect_number_array[i] + '2')

            perfect_number_array = temp_array
            current_count += len(perfect_number_array)

        current_count = current_count // 2

        while current_count < A:
            perfect_number_array.pop(0)
            current_count += 1

        print(perfect_number_array[0])
A = 40
Solution().solve(A)