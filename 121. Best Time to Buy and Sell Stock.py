def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        profit = 0
        for i in prices:
            if i<buy_price:
                buy_price = i
            elif i-buy_price>profit:
                profit = i-buy_price
        return profit
