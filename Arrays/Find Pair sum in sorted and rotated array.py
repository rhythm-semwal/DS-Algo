'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is the number of elements in array
'''


def findPairSum(arr, target):
    n = len(arr)

    # Finding pivot element (smallest elements position)
    low = 0
    high = n - 1
    pivot = 0

    while (low <= high):

        # To avoid the overflow
        mid = ((high - low) // 2) + low

        # First case mid is largest element
        if (mid < high and arr[mid + 1] < arr[mid]):
            pivot = mid + 1
            break

        # Mid is the smallest element
        if (mid > low and arr[mid - 1] > arr[mid]):
            pivot = mid
            break

        # Deciding the side to search further
        # Case when pivot is in right side
        if (arr[high] < arr[mid]):

            low = mid + 1

        else:

            high = mid - 1

    st = pivot

    # We will rotate as end may become less than 0
    end = (n + pivot - 1) % n

    # Using two pointer technique to find sum
    while (st != end):

        temp = arr[st] + arr[end]

        if (temp == target):

            return True

        elif (temp < target):

            st = (st + 1) % n

        else:
            end = (n + end - 1) % n

    return False


# approach 2
def findPairSum(arr, target):
    n = len(arr)

    # Using unordered_map to store already encountered number
    myMap = {}

    for i in range(n):

        req = target - arr[i]

        if req in myMap:
            return True

        myMap[arr[i]] = 1

    return False