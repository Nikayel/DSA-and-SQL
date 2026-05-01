class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #count to keep count, leftPointer, longestWindow
        count = {}
        left = 0
        longestWindow = 0
        result = 0
        # for loop
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            longestWindow = max(longestWindow, count[s[right]])
            if (right - left +1 ) - longestWindow > k:
                count[s[left]]-=1
                left+=1

            result = max(result, right-left+1)
        return (result)

        