class Solution:
    def isValid(self, s: str) -> bool:
        #valid paranthesis
        validParan = {')':'(','}':'{',']':'['}
        stack = []

        #loop over the s array:
        for i in range(len(s)):
            if s[i] in '([{':
                stack.append(s[i])
            elif not stack:
                return False
            else:
                opening = stack.pop()
                if opening != validParan[s[i]]:
                    return False
        return not stack
                