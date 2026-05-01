class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #have two pointers left,right -> 0 , 1
        left,right = 0,1
        #maxProfit = 0
        maxProfit = 0
        #while left < right: if prices[left] > prices[right] -> left +=1, right+=1
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right+=1
        #else:
            else:
        # currProfit = prices[right] - prices[left]
                currProfit = prices[right] - prices[left]
        #maxProfit = max(currProfit,maxProfit)
                maxProfit = max(currProfit,maxProfit)
                right+=1
        # right +=1
        return maxProfit

        #once done return 0