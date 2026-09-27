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
                if not stack:
                    return False
                topOfStack = stack[-1]
                if topOfStack == valid_p[bracket]:
                    stack.pop()
                else:
                    return False
            #if openning add to stack
            else:
                stack.append(bracket)
        #if nto stack return True else False
        return len(stack) == 0