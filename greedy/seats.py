class Solution:
    # @param A : string
    # @return an integer
    # method1
    # t.c = O(N)
    # s.c = O(1)
    @staticmethod
    def get_number_of_persons(arr, n):
        count = 0
        for i in range(n):
            if arr[i] == 'x':
                count += 1

        return count

    @staticmethod
    def get_mid_position(arr, n, num_of_persons):
        # +1 because count starts from 0
        mid = (num_of_persons+1)//2
        count = 0

        for i in range(n):
            if arr[i] == 'x':
                count += 1
                if count == mid:
                    return i

    def seats(self, A):
        n = len(A)
        no_of_persons = self.get_number_of_persons(A, n)

        if no_of_persons <= 1:
            return 0

        mid = self.get_mid_position(A, n, no_of_persons)
        result = 0
        i, j = 0, mid

        while i < j:
            if A[i] == 'x' and A[j] == '.':
                A[j] = A[i]
                A[i] = '.'
                result += j-i
                i += 1
                j -= 1
            elif A[j] == 'x':
                j -= 1
            else:
                i += 1

        i, j = n-1, mid
        while j < i:
            if A[i] == 'x' and A[j] == '.':
                A[j] = A[i]
                A[i] = '.'
                result += i-j
                i -= 1
                j += 1
            elif A[j] == 'x':
                j += 1
            else:
                i -= 1

        return result%10000003

    # method 2
    # T.C = O(N)
    # S.C = O(N)
    def seats(self, A):
        n = len(A)
        count_array = []

        for i in range(n):
            if A[i] == 'x':
                count_array.append(i)

        print(count_array)

        mid = len(count_array) // 2
        result = 0

        left, right = mid-1, mid+1
        k = 1

        while left >= 0:
            result += (count_array[mid]-k) - count_array[left]
            k += 1
            left -= 1

        k = 1
        while right < len(count_array):
            result += count_array[right] - (count_array[mid]+k)
            k += 1
            right += 1

        print(result)


A = "....xxx"
Solution().seats(A)
