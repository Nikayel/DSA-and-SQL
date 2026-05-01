class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #loop over each number and get the freq of each 
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        # freq {} -> {1:1,2:2,3:3}
        
        #do our bucket:
        res =[]
        bucket = [[] for _ in range(len(nums)+1)]
        for i,num in freq.items():
            bucket[num].append(i)
        
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res


            
            
            

        #store each number as value and they key would be the freq
        #loop over from the last item and add to result array until arra length = k