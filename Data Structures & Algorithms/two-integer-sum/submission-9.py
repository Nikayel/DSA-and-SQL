class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_idx = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen_idx:
                return [seen_idx[diff], i]
            seen_idx[n] = i
        return []