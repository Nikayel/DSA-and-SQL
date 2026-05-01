class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left and right pointer
        left,right = 0,len(nums)-1
        #loop over nums until in bound
        while(left<=right):
            #find the middle
            middle = (left+right)//2
            #if middle == target --> return  middle
            if(nums[middle] == target):
                return middle
            #if middle>target --> left = middle+1
            elif(nums[middle]>target):
                right = middle-1
            #else middle < target --> right = middle-1 ther other way around
            else:
                left = middle+1
        #return -1
        return -1
        