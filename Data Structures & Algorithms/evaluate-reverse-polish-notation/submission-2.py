class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Use stack to add or remove and return the value
        #Loop over each item
        #Edge case:
        # minus operand 
        stack = []
        for token in tokens:
            if token == "+":
                #could we have condition where starting point is an operand
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[0]


                
            
        