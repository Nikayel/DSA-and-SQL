class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #seen set 
        seen = set()
        #maxLength
        maxLength = 0

        #left
        left = 0
        #Loop using right pointer over the s array
        for right in range(len(s)):
            #Check if s[right] in seen
            while s[right] in seen:
                #move the left pointer
                seen.remove(s[left])
                left+=1
            #add the right pointer into the array and update/recac the maxLength
            seen.add(s[right])
            maxLength = max(maxLength, right - left+1)
            # currLength = right - left +1 
        #return maxlength
        return maxLength


        