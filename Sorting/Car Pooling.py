# https://leetcode.com/problems/car-pooling/
# TC = O(n log n)	
# SC = O(n)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from collections import defaultdict

        changes = defaultdict(int)

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers
        
        current_passengers = 0

        for location in sorted(changes.keys()):
            current_passengers += changes[location]

            if current_passengers > capacity:
                return False
        
        return True
        
