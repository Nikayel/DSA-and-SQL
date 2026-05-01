class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #left and right pointer -(k Is between max and 1)-
        left,right = 1,max(piles)
        result = 0
        #Loop until in bound
        while(left<=right):
            #find the middle
            middle = (left+right)//2
            hours = 0
            #devide each item in the array over our middle
            for i in piles:
                hours+= math.ceil(float(i/middle))
            #if sum of all is smaller than h -- new minimum min value
            if hours <= h:
                result = middle
            #also shift to the smaller side 
                right = middle-1
            #else --> shift to the right side
            else:
                left = middle+1
        #return k
        return result


        