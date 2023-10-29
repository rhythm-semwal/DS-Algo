class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        use property that (a+b)%m = 0
        (a%m + b%m)%m = 0
        so calculate a%m first
        store it in count array

        then find a+b pair
        special case when a == b and a%m == 0
        :param A:
        :param B:
        :return:
        """
        count_array = [0]*B

        for i in range(len(A)):
            rem = A[i]%B
            count_array[rem] += 1

        pairs = 0
        mod = 1000000007
        # for 0 remainder
        # //2 for the duplicate pairs
        # use ncr formula
        pairs += (count_array[0]*(count_array[0]-1))//2
        i, j = 1, B-1
        while i <= j:
            if i == j:
                pairs += (count_array[i]*(count_array[i]-1))//2
                pairs = pairs%mod
            else:
                pairs += count_array[i] * count_array[j]
                pairs = pairs % mod

            i += 1
            j -= 1

        print(pairs)


A = [5, 17, 100, 11]
B = 28

A = [1, 2, 3, 4, 5]
B = 2
print(Solution().solve(A, B))
