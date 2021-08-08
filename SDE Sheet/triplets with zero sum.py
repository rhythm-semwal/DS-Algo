# approach 1 - using hashing
# TC = O(N^2)
# SC = O(N)
# def findTriplets(arr,n):
#
#     result = []
#     for i in range(n-1):
#         hash_set = set()
#         for j in range(i+1, n):
#             temp = arr[i] + arr[j]
#
#             if -temp in hash_set:
#                 result.append([temp, arr[i], arr[j]])
#             else:
#                 hash_set.add(arr[j])
#
#     print(result)

# approach 2 - using sorting
"""
1) Sort the array in ascending order.
2) Traverse the array from start to end.
3) For every index i, create two variables l = i + 1 and r = n – 1
4) Run a loop until l is less than r, if the sum of array[l], array[r] is
equal to zero then print the triplet and break the loop
5) If the sum is less than zero then increment value of l,
by increasing value of l the sum will increase as the array is sorted, so array[l+1] > array [l]
6) If the sum is greater than zero then decrement value of r,
by increasing value of l the sum will decrease as the array is sorted, so array[r-1] < array [r].
"""


def findTriplets(arr, n):
    arr.sort()

    result = []
    for i in range(n-1):
        l = i+1
        h = n-1
        current_val = arr[i]

        while l < h:
            if current_val + arr[l] + arr[h] == 0:
                result.append((current_val, arr[l], arr[h]))
                l += 1
                h -= 1

            elif current_val + arr[l] + arr[h] < 0:
                l += 1

            else:
                 h -= 1

    print(result)


arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)
