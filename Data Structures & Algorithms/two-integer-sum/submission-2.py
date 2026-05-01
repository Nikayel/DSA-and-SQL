class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dict
        seen = {}
        #loop over each item in the array
        for i,num in enumerate(nums):
        #keep track of the INdex an the item
        #comapre the current item with our target and find the difference
            diff = target - num
        #if dict has the difference -> return index of curr and index of dic[diff]
            if diff in seen:
                return[seen[diff], i]
        #else add the curr to the dic
            seen[num] = i
        #return
        return