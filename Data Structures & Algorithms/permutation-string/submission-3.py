class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create empty array of 26 chars
        n1 = len(s1)
        n2 = len(s2)
        s1Array = [0] * 26
        s2Array = [0] * 26
        #edge case:
        #s2 smaller than s1
        if n2 < n1 :
            return False
        #populate them with len(s1) items
        for i in range(n1):
            #populate using their ASCII value
            s1Array[ord(s1[i]) - 97] +=1
            s2Array[ord(s2[i]) - 97] +=1

        #if s1array == 2array immedietly return True
        if s1Array == s2Array:
            return True

        #sliding window

        #leftpointer
        l = 0
        #loop over the s2 array starting from the end of len(s1) 
        for r in range(n1, n2):
        #shift the window to the right
            s2Array[ord(s2[r]) - 97] +=1
        #remove from the left then compare
            s2Array[ord(s2[l]) - 97] -=1
            l+=1
        #each iteration if return True if s1Array = s2Array
            if s1Array == s2Array:
                return True
        #loop ends return False
        return False