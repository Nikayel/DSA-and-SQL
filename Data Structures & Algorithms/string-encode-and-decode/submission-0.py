class Solution:

    def encode(self, strs: List[str]) -> str:
        #I should keep track of its length and add # before the string
        result = ""
        for s in strs:
            length = str(len(s))
            result += f"{length}#{s}"
        return result

    def decode(self, s: str) -> List[str]:
        #get the length of the word and find the # then append to result list
        result = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            result.append(s[j+1:length+j+1])
            i = j+1+length
        return result

