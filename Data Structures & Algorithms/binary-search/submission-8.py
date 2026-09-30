class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #left, right = 0, len(nums)
        left,right = 0, len(nums)-1
        while left <= right:
            #find the midpoint
            mid = left+((right-left )// 2)
            #figure out if target -> return index
            if nums[mid] == target:
                return mid
            #smaller then target -> move right
            elif nums[mid] < target:
                left = mid+1
            #bigger than target -> move left
            else:
                right = mid-1
        #return -1
        return -1