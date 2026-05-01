class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers left and right
        # left would be buy and right would be sell - left start from the first indez and right from the second index

        left = 0
        right = 1
        max_profit = 0
        #edge cases:
        #only one item return 0

        #only has 1 item
        # arr = [5,3,10,4,1,9,9,9]

        #loop over prices as long as valid

        # compare the left pointer and right pointer
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right]-prices[left]
                max_profit = max(max_profit, profit)
            right+=1
        return max_profit
                

            
                
        


        
        #