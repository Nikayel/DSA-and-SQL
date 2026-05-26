class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left and right vars -> 0, -1
        left,right = 0,len(nums)-1
        #Loop until in bound -> 
        while left <= right:
            #find the midpoint 
            mid = (left+right)//2
            #Case 1 left side sorted
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                #Sorted and target here
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                #sorted and target not here here
                else:
                    left = mid + 1 
            #Case 2 left not sorted
            else:
                #Sorted and target not here
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                #sorted and target here
                else:
                    right = mid -1
        return -1