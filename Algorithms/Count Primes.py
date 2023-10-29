# TLE error
class Solution1:
    """
    we reduce the numbers which needs to be checked to the square root of the given number.
    If the given number is divisible by any of the numbers from 2 to the square root of the number, the function will return False
    Else it will return True
    """
    def calculate(self, num):
        from math import sqrt
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        result = 0

        for num in range(2, n):
            ans = self.calculate(num)
            result += ans

        return result


class Solution2:
    """
    The thing to notice is that all the even numbers except two can not be prime number.
    In this method, we kick out all the even numbers to optimize our code and will check only the odd divisors.
    Following are the steps used in this method:

    If the integer is less than equal to 1, it returns False.
    If the number is divisible by 2, it will return True if the number is equal to 2 else false.
    Now, we have checked all the even numbers. Now, look for the odd numbers.
    If the given number is divisible by any of the numbers from 3 to the square root of the number
    skipping all the even numbers, the function will return False
    Else it will return True
    """
    def calculate(self, num):
        from math import sqrt
        if num % 2 == 0:
            return num == 2

        for i in range(3, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        result = 0

        for num in range(2, n+1):
            ans = self.calculate(num)
            result += ans

        return result


class Solution3:
    def countPrimes(self, n: int) -> int:
        prime = [True for _ in range(n+1)]

        p = 2
        while p*p <= n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1

        print(prime)

        result = 0
        for i in range(2, n):
            if prime[i]:
                result += 1

        return result

print(Solution3().countPrimes(10))