class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #hashmap
        counts,countt ={},{}
        #Loop over S and Ts length
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i],0) #j, a, r -> 1
            countt[t[i]] = 1 + countt.get(t[i],0) #j, a, m -> 1
                #get the count of each char
        return countt == counts
        #compare the char count