class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create dict
        res = {}

        #loop over each item in array
        for s in strs:
        #Create a list of 26 for each letter in AZ
            count = [0] * 26
        #loop over each char in the string
            for i in s:
        #get the count of each
                count[ord(i) - ord('a')] +=1 
        #if not yet exist -> Create 
            item = tuple(count)
            if item not in res:
                res[item] = []   
        #Add it to the dict
            res[item].append(s)
        #return result
        return list(res.values())
        