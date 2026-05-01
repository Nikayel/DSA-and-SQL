class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create an empty of zeros
        n1 = len(s1)
        n2 = len(s2)
        s1Count = [0] * 26
        s2Count = [0] * 26
        #edge case:
        # s2 < s1 return False
        if n2 < n1: return False
        #loop over the s1 length and populate the empty zero arrays
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] +=1
            s2Count[ord(s2[i]) - ord('a')] +=1
        #return True if initial popoulation(loop) makes s1==s2
        if s1Count == s2Count: return True

        # loop ( sliding window )
        for r in range(n1, n2):
            s2Count[ord(s2[r]) - 97] +=1
            s2Count[ord(s2[r-n1]) - 97] -=1

            if s1Count == s2Count:
                return True
        return False 
        #if anypoint of loop s1 == s2 return True
            


            
        



        