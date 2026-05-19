class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #first,second = 0,1
        #maxProfit = 0 - currProfit max(maxProfit,currProfit)
        #Time complexity On and space O1
        left,right = 0,1
        maxProfit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            currProfit = prices[right] - prices[left]
            maxProfit = max(currProfit,maxProfit)
            right+=1

        return maxProfit