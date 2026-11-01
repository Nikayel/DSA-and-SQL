class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx, num in enumerate(nums):
            need = target - num
            if need in visited:
                return [visited[need], idx]
            visited[num] = idx
        return 0