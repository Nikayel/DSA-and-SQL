class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a hashset for efficient search:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in num_set:
                current_longest = 1
                while num+1 in num_set:
                    num+=1
                    current_longest+=1
                longest = max(current_longest,longest)
        return longest


        