import random

N = 100000
INF = 1 << 46

Hash = {}


def rand46():  # generates 46bit random number
    ret = 0
    ret |= random.randint(0, INF)
    x = (random.randint(0, INF))
    ret = ret | (x << 15)

    return ret


def set_hash(a):
    Hash.clear()
    n = len(a)
    for i in range(0, n):
        if Hash.get(a[i]) is None:  # consider multiple occurences
            Hash[a[i]] = rand46()
       
            
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        set_hash(A)

        print(Hash)
        prefix_sum = [0]*n
        
        prefix_sum[0] = Hash[A[0]]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + Hash[A[i]]

        print(prefix_sum)
        q = len(B)
        ans = [0] * q
        for i in range(0, q):
            if B[i][0] > 0:
                v1 = prefix_sum[B[i][1]] - (prefix_sum[B[i][0] - 1])
            else:
                v1 = prefix_sum[B[i][1]]

            if B[i][2] > 0:
                v2 = prefix_sum[B[i][3]] - (prefix_sum[B[i][2] - 1])
            else:
                v2 = prefix_sum[B[i][3]]

            if v1 == v2:
                ans[i] = 1
        

A = [1, 7, 11, 8, 11, 7, 1]
B = [
       [0, 2, 4, 6]
     ]
# A = [1, 3, 2]
# B = [
#    [0, 1, 1, 2]
#  ]
Solution().solve(A, B)
