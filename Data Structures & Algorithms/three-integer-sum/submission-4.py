class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Loop over the nums array
        # if duplicate we continue else - two pointers left and right
        #triplet array
        triplet = [] #To append the triplets
        #loop over nums
        nums.sort()
        for num in range(len(nums)-2):
            #we ignore if duplicate
            if num > 0 and nums[num] == nums[num-1]:
                continue
            #left and right pointer
            left,right = num+1,len(nums)-1
            while left < right:
                result = nums[num] + nums[left]+nums[right]
                if result == 0:
                    triplet.append([nums[num] , nums[left],nums[right]])
                    left+=1
                    right-=1
                    #Edge Case:
                    #duplicate left and right/or right
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
                elif result > 0:
                    right-=1
                else:
                    left+=1
        return triplet

        