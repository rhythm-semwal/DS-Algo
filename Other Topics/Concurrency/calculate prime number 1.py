from math import sqrt

class PrimeNumber:
    @staticmethod
    def calculate(number):
        if number % 2 == 0:
            return number == 2

        for i in range(3, int(sqrt(number))+1):
            if number % i == 0:
                return False
        return True

    def main(self, n):
        result = 0
        for each in range(2, n):
            ans = self.calculate(each)
            result += ans
        return result


print(PrimeNumber().main(10))
