class Solution:
    def isValid(self, s: str) -> bool:
        valid_paranthesis = {'{':'}', '[':']','(':')'}
        stack = []
        for p in s:
            if not stack and p in ')}]':
                return False
            else:
                if p in '({[':
                    stack.append(p)
                else:
                    value = stack.pop()
                    if p != valid_paranthesis[value]:
                        return False
        return True if not stack else False