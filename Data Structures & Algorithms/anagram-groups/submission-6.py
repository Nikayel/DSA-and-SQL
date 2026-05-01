class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        #loop over each string in the array - > loop 1
        for s in strs:
            #Get each char freq and store it as a tuple -> For loop
            freq = [0] * 26
            #Use the tuple as our Key - > Append the current s from loop 1
            for char in s:
                #Freq using the ASCII value of the character
                freq[ord(char) - ord('a')]+=1
            keyToAdd = tuple(freq)
            count[keyToAdd].append(s)
        #return the values of the count or result dict
        return list(count.values())