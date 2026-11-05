class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        buy = 0

        for sell in range(len(prices)):
            # 1. If we find a cheaper price, update our buy pointer
            if prices[sell] < prices[buy]:
                buy = sell
            # 2. Otherwise, calculate the profit and keep the highest one
            else:
                max_prof = max(max_prof, prices[sell] - prices[buy])

        return max_prof