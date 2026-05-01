class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create array of 26 letters 
        n1 = len(s1)
        n2 = len(s2)
        s1Count,s2Count = [0] * 26, [0]*26
        #edge case:
        # if s1 > s2 return False
        if n1 > n2:
            return False
        #populate the empty arrays - s1Count, s2Count
        for i in range(n1):
            s1Count[ord(s1[i]) - 97] +=1
            s2Count[ord(s2[i]) - 97] +=1
        #return s1Count == s2Count
        if s1Count == s2Count:
            return True
        #slide the window ( loop from the last item of s1 till end of s2 )
        for r in range(n1, n2):
        #for each iteration check if window valid if not keep looping
            s2Count[ord(s2[r])-97] +=1
            s2Count[ord(s2[r-n1]) - 97] -=1
            if s1Count == s2Count:
                return True
        #return False
        return False
            
        



        