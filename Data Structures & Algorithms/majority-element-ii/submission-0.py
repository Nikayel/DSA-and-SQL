class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freqMap = Counter(nums)
        
        for key in freqMap:
            if freqMap[key] > len(nums) // 3:
                res.append(key)
        return res