class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            delta = prices[right] - prices[left]
            if delta > 0:
                max_profit = max(delta, max_profit)
                right += 1
            else:
                left = right
                right += 1
        
        return max_profit
