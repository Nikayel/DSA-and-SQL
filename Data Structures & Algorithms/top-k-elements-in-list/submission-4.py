class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Build a frequency map
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        #Create a buckcet = [] * len(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        for num,count in freq.items():
            bucket[count].append(num)
        res = []
        #Loop over bucket from -1, move -1,
        for i in range(len(bucket)-1,0,-1):
            #append to result until result == k
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return -1