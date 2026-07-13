class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #1 + 2 -> 3 -> 3 --> 9 stkac - > 9 4 -> 
        #Stack
        result = []
        operators = {"+", "-", "*", "/"}
        #Loop over tokens
        for token in tokens: #5, 13 13/5 
            #if number add to stack
            if token in operators:
                a = result.pop()
                b = result.pop()
                if token == "+":
                    res = a+b
                elif token == "-":
                    res = b - a
                elif token == "*":
                    res = a * b
                else:
                    res = int(b/a)
                result.append(res)  
            #else pop 2 items from the stack
            else:
                result.append(int(token))
        #return stack
        item = result.pop()
        return item