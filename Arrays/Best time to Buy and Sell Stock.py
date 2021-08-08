class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        buy_price, sell_price = float('inf'), 0

        for price in prices:
            buy_price = min(price, buy_price)
            sell_price = max(price-buy_price, sell_price)

        return sell_price

a = [7,1,5,3,6,4]
print(Solution().maxProfit(a))


