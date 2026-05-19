class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left,right
        left,right = 0,0
        #length = 0
        length = 0
        #set
        seen = set()
        #loop over s
        for right in range(len(s)):
            #if s[i] in set:
            while s[right] in seen:
                #remove from set
                seen.remove(s[left])
                #move leftPointer
                left+=1
            #length = max(length,right-left+1)
            seen.add(s[right])
            length = max(length,right-left+1)
        #return length
        return length