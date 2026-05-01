class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Left and right pointer both starting from first item
        left,right = 0,0
        #set to keep track of duplicates or chara
        seen = set()
        longest=0
        #loop using for or while
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            else:
                seen.add(s[right])
                longest = max(longest,right-left+1)
        return longest

#set = y,z,x longest = 3, left = y
#