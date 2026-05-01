#we start the loop from th efirst element
#no duplicat should be considered
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)
        for num in range(n-2):
            if num > 0 and nums[num] == nums[num-1]:
                continue
            left,right = num+1, n-1
            while left < right:
                result = nums[left] + nums[right] + nums[num]
                if result == 0:
                    triplets.append([nums[left],nums[right],nums[num]])
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left+=1
                    right-=1
                elif result < 0 :
                    left +=1
                else:
                    right -=1
        return triplets
        