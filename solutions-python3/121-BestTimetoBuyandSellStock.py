# 121. Best Time to Buy and Sell Stock
# Idea:
#     1. 找到最小值，往後找最大值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]    # buy day
        priceAfterMinPrice = prices[1]   # sell day
        maxProfit = 0

        for priceAfterMinPrice in prices[1:]:
            curProfit = priceAfterMinPrice - minPrice
            
            if curProfit > 0:
                maxProfit = max(maxProfit, curProfit)
            else:
                minPrice = priceAfterMinPrice
        
        
        return maxProfit