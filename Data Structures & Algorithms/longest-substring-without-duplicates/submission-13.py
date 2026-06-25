class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left and right pointer
        l,r = 0,0
        #seen set then add/remove and move pointer
        seen = set()
        length = 0 
        #until in bound (while left < right)  
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            length = max(length,r - l+1)
            seen.add(s[r])
            r+=1
        return length
        # p added   seen = p,w
        # w added   
        # w remove and move l  