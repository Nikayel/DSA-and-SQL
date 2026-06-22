class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = []
        for indx,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[indx]:
                top = stack.pop()
                res[top] = indx - top
            stack.append(indx)
        return res
            
            
