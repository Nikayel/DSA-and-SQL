class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        Write_Cursor = 1
        for pointer in range(1, len(nums)):
            if nums[pointer] != nums[pointer - 1]:
                nums[Write_Cursor] = nums[pointer]
                Write_Cursor+=1
        return Write_Cursor
