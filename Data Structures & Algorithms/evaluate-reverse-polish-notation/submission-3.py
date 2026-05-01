class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack , and if number add to the stack
        stack = []
        #and if operator pop 2 itms from the stack 
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                answer = b - a 
                stack.append(answer)
            elif c == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
        # edge cases:
        # subtracting and since // -> trunncn -> 0 we can just say int(a//b)