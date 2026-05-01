class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create a stack
        stack = []
        res = [0] * len(temperatures)
        #res list -> keep track of curr till next high temp day
        #loop over the items in temperatures (if )
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stk_t,stk_i = stack.pop()
                res[stk_i] = i - stk_i
            stack.append((t,i))
        return res
        
            
            