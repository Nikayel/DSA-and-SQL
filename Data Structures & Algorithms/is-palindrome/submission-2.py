class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Have two pointers
        left,right = 0,len(s)-1

        #start left pointer from index 0 and right pointer from index -1(last) and move inwards
        #continue until left and right collide
        s = s.lower()
        while left < right:
            while left < right and not s[left].isalnum():
                left+=1
            while left < right and not s[right].isalnum():
                right-=1
            if s[left] != s[right]:
                return False
            else:
                left +=1
                right-=1
        return True
        #aba
        