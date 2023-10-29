"""
Approach: Total numbers in the range will be (R – L + 1) i.e. N.  

1. If N is even then the count of both odd and even numbers will be N/2.
2. If N is odd, 
  a. If L or R is odd, then the count of the odd numbers will be N/2 + 1, and even numbers = N – countofOdd.
  b. Else, the count of odd numbers will be N/2 and even numbers = N – countofOdd.
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low + 1

        if n % 2 == 0:
            return n // 2
        else:
            if low % 2 != 0 or high % 2 != 0:
                return (n//2)+1
            else:
                return n // 2
