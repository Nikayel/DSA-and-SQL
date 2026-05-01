class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [5,4,3,0,1,2]
        #left and right
        left,right = 0,len(nums)-1

        #loop over until left and right pointer meet
        while left < right:
            middle = (left+right)//2

        #if the middle pointer is bigger than the last item(right), we can uignore everything on the left and just loo to the right
            if nums[middle] > nums[right]:
                left = middle +1
        #else we can move the right pointer to be the middle pointer
            else:
                right = middle

        #then return the smallest
        return nums[left]
                
        