class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #longest_substring = 0
        #left = 0
        #set() = s
        longest_substring = 0
        left = 0
        sset = set()
        #loop over the s
        for right in range(len(s)):

                #If in the set pop()
                while s[right] in sset:
                    sset.remove(s[left])
                    left+=1
                current_length = (right-left)+1
                longest_substring = max(longest_substring, current_length)
                sset.add(s[right])
        return longest_substring




                #calculate the current length
            
            #compare current length with max_length
            
            #add the current value to the set

        