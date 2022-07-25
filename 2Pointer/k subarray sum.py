class Solution:
    def k_subarray_sum(arr, k):
        result_array = []
        current_sum = sum(arr[:k])
        result_array.append(current_sum)

        for i in range(k, len(arr)):
            current_sum = current_sum - arr[i-k] + arr[i]
            result_array.append(current_sum)

        return result_array    


if __name__ == '__main__':
    arr = [3, 5, 6, 2, 4, 7, 8]
    k = 3
    print(Solution.k_subarray_sum(arr, k))