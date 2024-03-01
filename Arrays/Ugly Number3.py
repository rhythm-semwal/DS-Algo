class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ugly = [1]

        x, y, z = 0, 0, 0

        while len(ugly) < n+1:

            next = min(ugly[x] * a, ugly[y] * b, ugly[z] * c)

            ugly.append(next)

            if next == ugly[x] * a:
                x += 1

            if next == ugly[y] * b:
                y += 1

            if next == ugly[z] * c:
                z += 1

        print(ugly)
        return ugly[-1]


n = 5
a = 2
b = 11
c = 13
print(Solution().nthUglyNumber(n, a, b, c))

