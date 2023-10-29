# min coins to get target sum

class Solution:
    def coinChange(self, coins, amount: int) -> int:

        import sys
        dp_list = [sys.maxsize] * (amount + 1)
        dp_list[0] = 0  # base case condition

        for i in range(1, amount + 1):
            min_coin = sys.maxsize
            for coin in coins:
                if coin <= i:
                    temp = dp_list[i - coin]
                    if temp != sys.maxsize:
                        min_coin = min(min_coin, temp + 1)
            dp_list[i] = min_coin
        if dp_list[-1] == sys.maxsize:
            return -1
        return dp_list[-1]
