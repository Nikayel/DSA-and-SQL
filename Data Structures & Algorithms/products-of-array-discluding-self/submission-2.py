class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Answer array of length nums containing 1 -> res
        n = len(nums)
        res = [1] * n
        #Loop and get the prefix
        prod = 1
        for i in range(n):
            res[i] = prod
            prod *= nums[i]

        #loop and get postfix
        prodRight = 1
        for p in range(n-1,-1,-1):
            res[p] *= prodRight
            prodRight *=  nums[p] #second pass -> 24
        return res

        #return res array

        #1,1,2,8

        #PostFix - > Product = 8, res[ ,8]
