class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_C_S = 0
        if not nums:
            return longest_C_S
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current = num
                count = 1
                while current+1 in num_set:
                    count += 1
                    current+=1
                longest_C_S = max(count, longest_C_S)
        return longest_C_S
            #2,20,4,10,3,5
    