class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #output
        output = []
        left_prod = 1
        #left side mutliply
        for i in range(0,len(nums)):
            output.append(left_prod)
            left_prod*=nums[i]
        #output = [1,1,4,8]
        #right side multiply 
        right_prod = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= right_prod
            right_prod *=nums[i]
        return output