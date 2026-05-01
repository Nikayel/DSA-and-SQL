class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #output array
        output = [1] * (len(nums))
        #left =1
        left = 1
        #loop ov er the array and * each item with its left
        for i in range(len(nums)):
            output[i] = left
            left *= nums[i] #left = 4
        #output = [1,1,2,8]
        #----2nd Loop
        #right = 1
        #loop over the array 
        right = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= right
            right *=nums[i]
        #output[...12,8]
        return output

     
        