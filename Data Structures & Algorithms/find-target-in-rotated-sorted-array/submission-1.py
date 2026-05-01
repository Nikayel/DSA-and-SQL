class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left and right pointer
        left,right = 0,len(nums)-1
        #loop over the nums array until in bound
        while(left<=right):
            #find the middle
            middle = (left+right)//2
            #check if middle --> target = return middle
            if nums[middle] == target:
                return middle
            #check if left is sorted
            if nums[left]<=nums[middle]:
                #--> is it not in the range? -- > search
                if target>nums[middle] or target<nums[left]:
                    left = middle+1
                #--> in the range --> move to the right half
                else:
                    right = middle-1
            #if not sorted move accordingly
            else:
                if target<nums[left] and target>=nums[right]:
                    left = middle+1
                else:
                    right = middle-1 
        return -1


