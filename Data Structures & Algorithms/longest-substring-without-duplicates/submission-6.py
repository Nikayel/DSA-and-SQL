class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    #Set
        seen = set()
    #maxLength
        maxLength = 0
    #Left, right -> 1st item[0]
        left,right = 0,0
    #loop over the array 
        for right in range(len(s)):
            while s[right] in seen:
                #if s[right] in seen set > remove from the set and move left
                seen.remove(s[left])
                left+=1
    #edge case:
    #using a loop and remove until we find new non-repeating. 
    #add to set(s[right])
            seen.add(s[right])
    #recalc maxLenth > max(maxLength,right-left+1)
            maxLength = max(maxLength,right-left+1)
    #return maxLength
        return maxLength