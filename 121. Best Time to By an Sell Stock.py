# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_buy = -1
        for price in prices:
            if price < min_buy or min_buy == -1:
                min_buy = price
            else:
                max_profit = max(max_profit, price - min_buy)
        return max_profit
