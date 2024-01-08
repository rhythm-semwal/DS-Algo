class Solution1:
    def firstMissingPositive(self, nums) -> int:
        """
        Step 1 -> The main idea behind it is that the minimum number to be found will always be in the range [1....n]
        where 'n' is the length of list.
        So keep numbers in this range and mark others(here we are marking them with (n+1) value) in the list provided.
	    """

        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1

        '''Step 2 -> Ignoring the values greater than 'n', mark the indexes of the numbers in the range [1...n]
					 so as to ensure that this values are present. To mark the indexes, 
					 I am negating the value present at that index.'''

        for i in range(n):
            val = abs(nums[i])
            if val > n:
                continue
            val -= 1  # since the list is zero indexed,so every value will be at position val - 1

            if nums[val] > 0:
                # For similar numbers, it will keep on fluctuating between negative and positive
                # which is not our motive here.

                nums[val] = -1 * nums[val]

        '''Step 3 -> Return the first occurence of the non-negative numbers from the list'''

        for i in range(n):
            if nums[i] >= 0:
                return (i + 1)  # bcoz list is zero indexed

        '''Step 4 -> We will encounter this if no positives were found. This means that all the 
			         numbers are in the range [1....n]. So the missing positive number will be n+1'''

        return (n + 1)


class Solution2:
    """
    @param A: An array of integers
    @return: An integer
    """

    def firstMissingPositive(self, A):
        # write your code here
        n = len(A)

        i = 0

        while i < n:
            print(A[A[i]-1])
            while 0 < A[i] <= n and A[A[i] - 1] != A[i]:
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp

            i += 1

        for index, value in enumerate(A):
            if index + 1 != value:
                return index + 1

        return n + 1


class Solution3:
    def firstMissingPositive(self, A):
        contains_one = False
        n = len(A)
        for i in range(n):
            if A[i] == 1:
                contains_one = True

            elif A[i] <= 0 or A[i] > n:
                A[i] = 1

        if not contains_one:
            return 1

        i = 0
        while i < n:
            if A[i] != A[A[i] - 1]:
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp
            else:
                i += 1

        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1


if __name__ == "__main__":
    arr = [4, 3, 2, 1]
    print(Solution2().firstMissingPositive(arr))
