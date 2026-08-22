class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(':')', '{':'}','[':']'}
        stack = []
        for i in range(len(s)):
            if not stack and s[i] in '})]':
                return False
            if s[i] in "([{":
                stack.append(s[i])
            else:
                toCompare = stack.pop()
                if valid[toCompare] != s[i]:
                    return False
        return True if not stack else False
            
                
            
