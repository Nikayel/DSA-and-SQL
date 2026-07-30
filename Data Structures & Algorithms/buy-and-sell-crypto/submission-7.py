class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        highest = 0
        if not prices:
            return 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                curr_profit = prices[right] - prices[left]
                highest = max(highest, curr_profit)
                right+=1
        return highest
            