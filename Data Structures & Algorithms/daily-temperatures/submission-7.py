class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #stack
        stack =[]
        #res
        res =[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stk_i,stk_t = stack.pop()
                res[stk_i] = i - stk_i
            
            stack.append((i,t))
        return res