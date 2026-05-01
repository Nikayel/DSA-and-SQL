class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #left,rgiht
        left,right = 0,0
        #maxSubstring = 0
        maxSub = 0
        #chars = set()
        chars = set()
        #as long as right:
        for right in range(len(s)):
        #if s[right] in chars:
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            else:
                chars.add(s[right])
                maxSub = max(maxSub,right-left+1)

        return maxSub



        

        
