class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #result 
        n = len(temperatures)
        result = [0] * n
        #Visted
        stack = []
        #loop over the temepratures
        for i in range(n):
            #check if valid the continue 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                oldTempIndx = stack.pop()
                result[oldTempIndx] = i - oldTempIndx
            stack.append(i)
            #Add the new to the stack
        #return the result
        return result
