class Solution:
    # @param A : list of integers
    # @return a list of integers
    """
    if prefix(0,x) == prefix(0,y)
               =>  sum of subarray from (x+1) to (y) is zero . arr[x+1,y]=0
    Now if at any point prefix_sum==0 , ie subarray from (0) to (y) is zero
        => that's why we set first_occ[0]=-1;
            coz starting se y point tk is zero array and length of that array will be = y - (-1).
            here y represents the index at point where prefix sum becomes zero.
    """
    def lszero(self, A):
        start, end = -1, -1
        max_subarray_length = 0
        current_sum = 0
        sum_dict = {0: -1}

        for index, value in enumerate(A):
            current_sum += value

            if current_sum in sum_dict:
                if max_subarray_length < index-sum_dict[current_sum]:
                    max_subarray_length = index - sum_dict[current_sum]
                    start = sum_dict[current_sum]+1
                    end = index
            else:
                sum_dict[current_sum] = index

        return A[start:end+1] if max_subarray_length else []


A = [1 ,2 ,-2 ,4 ,-4]
A = [15,-2,2,-8,1,7,10,23]
A = [2, -2]
print(Solution().lszero(A))
