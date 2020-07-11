class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = 2147483647
        
        for x in range(0, len(prices)):
            if prices[x] < min_value:
                min_value = prices[x]
            elif prices[x] - min_value > max_profit:
                max_profit = prices[x] - min_value
                
        return max_profit