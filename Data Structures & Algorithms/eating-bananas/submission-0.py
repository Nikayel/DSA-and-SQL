import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 0
        #left and right pointer
        left,right = 1,max(piles)
        #loop top find middle value intil in the range(valid)
        while left<=right:

            total_time = 0
            k =(left+right)//2
            for p in piles:
                total_time += math.ceil(float(p)/k)
            if total_time <= h:
                result = k
                right = k-1
            else:
                left = k+1
        return result


        # inside the loop, loop p in piles - add to totalTime it gets each time we loop
        
        #compare and ecode to move to the left or to the right
