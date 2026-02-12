# https://leetcode.com/problems/corporate-flight-bookings/description/
# O(n + k) where n = number of flights and k = number of bookings
# Approach: Use a difference array and then calculate the running sum
# Mark the start-1 with the seats
# Then mark the end with -seats, which is not a part of the booking, so when calculating the running sum, we remove the seats

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0]*(n+1)

        for start, end, seats in bookings:
            result[start-1] += seats
            result[end] -= seats

        for i in range(1, n):
            result[i] += result[i-1]

        return result[:n]
