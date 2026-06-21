class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #hashmap
        seen = {}
        #loop over nums - > enumerate (Index)
        for indx,num in enumerate(nums):
            #Check if current exists in hasmap and compare i == j
            if num in seen:
                #if yes - > abs(i - j) <= k:
                distance = abs(seen[num] - indx)
                    #return True
                if distance <= k:
                    return True                    
            #else:
                #hashmap  - > hasmap[num] = indx
            seen[num] = indx
        return False
        #return False