from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create defaultdictionry
        #loop over the array:
        #create 26 zeros to keep count and freq of each character
        # loop c in each letter
        # find the poisiton and add to it's freq by comparing c to 'a'
        # convert it to a tuple - store in the key
        # exit the first loop
        # the defaultdictioney[key] we add the s ( so same keys would go in the same bracket)
        # end loop return the default dictioeny
        result = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')]+=1
            keyToAppend = tuple(count)
            result[keyToAppend].append(s)
        return result.values()

            
