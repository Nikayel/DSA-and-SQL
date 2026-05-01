class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arrayResult = [0]*len(temperatures)
        stack = []
        #loop over the temperatures index and item
        for i,t in enumerate(temperatures):
            #If the current item is bigger than the stack item keep checking and popping the last item and find its index and how many days to warmer temp
            while stack and t > stack[-1][0]:
                stackT,stackI = stack.pop()
                arrayResult[stackI] = i - stackI
            stack.append((t,i))
        return arrayResult