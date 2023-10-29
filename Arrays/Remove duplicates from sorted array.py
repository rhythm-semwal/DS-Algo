class Solution1:
    # TC = O(N)
    # SC = O(N)
    def removeDuplicates(self, arr) -> int:
        index = 0
        n = len(arr)

        if n <= 1:
            return n

        for i in range(n-1):
            if arr[i] != arr[i+1]:
                arr[index] = arr[i]
                index += 1

        arr[index] = arr[-1]
        index += 1

        return index

class Solution2:
    # TC = O(N)
    # SC = O(N)
    def removeDuplicates(self, arr) -> int:
        # write your awesome code here
        n = len(arr)

        if n == 1:
            return arr

        slow, fast = 0, 1
        result = []

        while fast < n:
            if arr[slow] != arr[fast]:
                result.append(arr[slow])
            fast += 1
            slow += 1

        result.append(arr[slow])
        for i in range(0, len(result)):
            arr[i] = result[i]

        return len(result)