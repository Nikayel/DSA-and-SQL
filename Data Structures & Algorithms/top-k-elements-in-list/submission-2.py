class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] =1
        bucket = [[] for i in range(len(nums)+1)]
        for key,value in count.items():
            bucket[value].append(key)
            # array = 0, 1(1), 2(2), 3(3,2), ... 6(0)
        
        res = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res





        