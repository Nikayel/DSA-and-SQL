class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 1
        output = 0
        if len(prices) < 2:
            return output
        
        for i in range(len(prices)-1):
            if prices[sell] < prices[buy]:
                buy = sell
                sell+=1
            else:
                curr_profit = prices[sell] - prices[buy]
                output = max(output,curr_profit)
                sell+=1
        return output

        