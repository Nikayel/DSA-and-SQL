class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #max 
        prevmax = 0
        #loop over the entire heights
        left,right = 0,len(heights)-1
        while left < right:
            #caculate and compare curr max with prev max
            newmax = min(heights[left],heights[right]) * (right-left)
            prevmax = max(newmax,prevmax)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1        
        return prevmax
        #move


