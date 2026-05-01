class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # empty stack
        temp = [0] * len(temperatures)
        stack = []
        #loop over the temperature
        for i,t in enumerate(temperatures):
                #check if stack has an item and if so check if its warmer temp than current temp
                    while stack and stack[-1][0] < t:
                        tempp,indexx = stack.pop()
                        temp[indexx] = i-indexx
                    #check the distance of current temp with the temp in the stack
        #add to the stack
                    stack.append((t,i))
        return temp

                    
        
        
            

            