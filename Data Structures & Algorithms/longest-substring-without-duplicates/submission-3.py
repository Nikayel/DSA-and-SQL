class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left pointer 
        left = 0    
        #maxlength
        maxlength = 0
        #set to keep track of our items
        seen = set()
        #loop over the lenght of th array
        for right in range(len(s)):
        #if this item exists - > if not exist add it to our set 
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxlength = max(maxlength,right-left+1)
        return maxlength
        #maxLength max(maxLenght, right-left+1)

        #return maxLength