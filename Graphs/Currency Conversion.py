class Solution:
    def has_arbitrage(self, currencies, rates):
        # currencies: list of currency names
        # rates: list of (from, to, rate)
        import math

        idx = {value: index for index, value in enumerate(currencies)}

        edges = []
        for u, v, rate in rates:
            edges.append((idx[u], idx[v], -math.log(rate)))

        dist = [0]*len(currencies)
        for _ in range(len(currencies)-1):
            for u, v, rate in edges:
                if dist[u] + rate < dist[v]:
                    dist[v] = dist[u] + rate

        for u, v, rate in edges:
            if dist[u] + rate < dist[v]:
                return True

        return False

if __name__ == "__main__:
  currencies = ["USD", "EUR", "GBP"]

  rates = [
        ("USD", "EUR", 0.9),
        ("EUR", "GBP", 0.8),
        ("GBP", "USD", 1.9)
    ]

  print(Solution().has_arbitrage(currencies, rates))
