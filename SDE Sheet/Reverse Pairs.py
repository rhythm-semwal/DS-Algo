class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self, A, low, mid, high):
        count = 0
        j = mid+1

        for i in range(low, mid+1):
            while j <= high and A[i] > (2*A[j]):
                j += 1

            # for every value of left array increment the value of count
            count += j-(mid+1)

        temp_array = list()
        left = low
        right = mid+1

        while left <= mid and right <= high:
            if A[left] <= A[right]:
                temp_array.append(A[left])
                left += 1
            else:
                temp_array.append(A[right])
                right += 1

        while left <= mid:
            temp_array.append(A[left])
            left += 1

        while right <= high:
            temp_array.append(A[right])
            right += 1

        for i in range(low, high+1):
            A[i] = temp_array[i-low]

        return count

    def merge_sort(self, A, low, high):
        if low >= high:
            return 0

        mid = (low+high)//2
        result = self.merge_sort(A, low, mid)
        result += self.merge_sort(A, mid+1, high)
        result += self.merge(A, low, mid, high)
        return result

    def solve(self, A):
        return self.merge_sort(A, 0, len(A)-1)


A = [1, 3, 2, 3, 1]
print(Solution().solve(A))
