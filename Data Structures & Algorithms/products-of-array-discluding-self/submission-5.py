class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left_prod = 1
        for i in range(len(nums)):
            output.append(left_prod)
            left_prod *= nums[i]
        right_prod = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= right_prod
            right_prod *=nums[i]
        return output