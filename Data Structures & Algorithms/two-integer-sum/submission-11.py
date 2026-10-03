class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap
        visited = {}
        #loop with idx and num on nums array
        for idx,num in enumerate(nums):
            #get the target difference
            diff = target - num
            #Check if in hasmap 
            #exists -> return curr IDX and diff IDX
            if diff in visited:
                return [visited[diff], idx]
            #!exists -> "key(num): value(idx)"
            else:
                visited[num] = idx # 3: 0 return 0, idx
