class Solution:
    def isValid(self, s: str) -> bool:
        #[[[]]
        #define what valid paranth is
        valid_p = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        #stack
        stack = []
        #loop over the array s
        for bracket in s:
            #if (closing) compare wiht top of stack
            if bracket in valid_p:
                #if not valid[current(})] == stack[-1]({)
                
                if not stack or stack[-1] != valid_p[bracket]:
                    return False
                else:
                    stack.pop()
            #if openning add to stack
            else:
                stack.append(bracket)
        #if nto stack return True else False
        return len(stack) == 0