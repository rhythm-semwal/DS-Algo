# https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        
        for source, destination, cost in flights:
            graph[source].append((destination, cost))
        
        queue = deque()
        # source, cost, stops
        queue.append((src, 0, 0))
        
        min_costs = [float('inf')] * n
        min_costs[src] = 0

        ans = float('inf')

        while queue:
            city, cost, stop = queue.popleft()

            if city == dst:
                ans = min(ans, cost)
                continue
            
            if stop > k:
                continue
            
            for next_city, price in graph[city]:
                new_cost = cost + price

                if new_cost >= ans:
                    continue
                
                if new_cost < min_costs[next_city]:
                    min_costs[next_city] = new_cost
                    queue.append((next_city, new_cost, stop+1))
        
        return -1 if ans == float('inf') else ans
