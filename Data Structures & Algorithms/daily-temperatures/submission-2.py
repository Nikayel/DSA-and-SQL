class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack to store the temperature Temprry
        stack =[]
        #empty array to store the results
        result = [0]*len(temperatures)
        #loop over temperatures
        for i,t in enumerate(temperatures):
            #check for potential warmer day
            while stack and t > stack[-1][0]:
                stackT,stackI = stack.pop()
                result[stackI]= i-stackI
            
            #if warmer append to result by using th eindex of current and the array index
            #append to the stack
            stack.append((t,i))
        return result

