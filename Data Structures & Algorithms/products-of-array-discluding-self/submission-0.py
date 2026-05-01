class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        left = 1
        for i in range(length): #left = 1,1,2,8,48
            result[i] = left #result = 1,1,
            left*=nums[i]
        right =1
        for i in range(length-1,-1,-1):
            result[i] *=right
            right *=nums[i]
        return result

     