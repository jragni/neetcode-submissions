class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            delta = sell - buy
            max_profit = max(delta, max_profit)
            if delta <= 0:
                left = right
            right += 1
        return max_profit
