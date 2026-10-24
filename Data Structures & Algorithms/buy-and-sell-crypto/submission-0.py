class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_buy = float('inf') 
        max_profit =  0
        
        for i in range(len(prices)):
            if prices[i] < lowest_buy:
                lowest_buy = prices[i]
            curr = prices[i] - lowest_buy
            if curr > max_profit:
                max_profit = curr

        return max_profit