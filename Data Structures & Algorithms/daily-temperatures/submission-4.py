class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Create a stack
        stack = []
        res = [0] * len(temperatures)
        #res list -> keep track of curr till next high temp day
        #loop over the items in temperatures (if )
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stk_i,stk_t = stack.pop()
                res[stk_t] = i - stk_t
            stack.append((t,i))
        return res
        
            
            