class Solution:
    def isValid(self, s: str) -> bool:
        #define what valid openToClose look like
        validParan = {')':'(','}':'{',']':'['}
        stack = []
        #edge cases:
        # empty array,
        # Only 1 paranthesis 

        #[][][[]]
        #Loop over the s array and if its an openning add to stack ese comapre
        #at any point if we see invalid return False
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                item = stack.pop()
                if validParan[s[i]] != item:
                    return False
        return True if not stack else False
        #return True if Stack is empty else False
        