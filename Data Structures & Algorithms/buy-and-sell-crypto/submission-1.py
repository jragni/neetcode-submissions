class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = left = right = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            if profit <= 0:
                left = right
            
            right += 1
        
        return max_profit