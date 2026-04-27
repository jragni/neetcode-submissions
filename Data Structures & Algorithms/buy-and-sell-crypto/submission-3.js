class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let bestProfit = 0;
        let sell = 0;
        let buy = 0;
        while (sell < prices.length) {
            if (prices[sell] - prices[buy] < 0) {
                buy = sell;
            }
            bestProfit = Math.max(bestProfit, prices[sell] - prices[buy]);
            sell++;
        }
        return bestProfit;
    }
}
