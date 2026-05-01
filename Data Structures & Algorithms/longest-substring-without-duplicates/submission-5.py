class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #visited/seen
        seen = set()
        #maxLength
        maxLength = 0
        left = 0
        #loop over the entire array
        for right in range(len(s)):  #maxLength = 2, set = [w,w]
            #if visisted:
            while s[right] in seen:
                #remove the item that we visited
                seen.remove(s[left])
                #move the left window
                left+=1

            #seen.add(currItem)
            seen.add(s[right]) #seen = (zx)
            #max(maxLength,currLength (right - left +1))
            maxLength = max(maxLength,right-left+1) #maxLenght = 1 2nd loop its 2
        #return maxLength
        return maxLength

        