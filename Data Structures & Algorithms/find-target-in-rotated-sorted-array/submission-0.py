class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left and right pointers
        left,right = 0, len(nums)-1
        #loop until in bound
        while(left<=right):
            #find the middle
            middle = (left+right)//2
            #if found return 
            if nums[middle] == target:
                return middle
            #check if left side is sorted 
            if nums[left] <= nums[middle]:
                #when sorted left side we see if not in that range
                if target<nums[left] or target > nums[middle]:
                    left = middle+1
                #if in the range 
                else:
                    right = middle-1
            #incase left side is not sorted
            else:
                #check if target is outside the range:
                if target > nums[right] or target<nums[middle]:
                    right = middle-1
                else:
                    left = middle+1
        return -1

        