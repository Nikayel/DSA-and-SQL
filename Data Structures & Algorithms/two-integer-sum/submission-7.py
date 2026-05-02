class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for indx,num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], indx]
            seen[num] = indx
        return