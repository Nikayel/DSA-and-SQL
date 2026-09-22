class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq.items():
            buckets[freq].append(num)
        
        for bucket in range(len(buckets)-1,-1,-1):
            for item in buckets[bucket]:
                if len(result) < k:
                    result.append(item)
                else:
                    break
        return result