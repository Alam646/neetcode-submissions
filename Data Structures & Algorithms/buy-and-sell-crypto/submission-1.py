class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        buy = 0

        for sell in range(len(prices)):
            
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                max_prof = max(max_prof, prices[sell] - prices[buy])
        
        return max_prof