class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        bucket = [[]for _ in range(len(nums)+1)];
        for key,value in freq.items():
            bucket[value].append(key)
        result = []
        for b in range(len(bucket)-1,0,-1):
            for j in bucket[b]:
                result.append(j)
                if len(result) == k:
                    return result
        
        

        
        
















































































































