# Using Dutch National Flag Algorithm.
# Order does not matter here
def reArrange(arr, n):
    low, high = 0, n - 1
    while low < high:
        if arr[low] < 0:
            low += 1
        elif arr[high] > 0:
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]


def displayArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print('')


arr = [1, 2, -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2, 1]
n = len(arr)
reArrange(arr, n)
displayArray(arr, n)

