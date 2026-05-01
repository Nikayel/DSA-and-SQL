class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res array and stack []
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                pstk_i,p_stk_t = stack.pop()
                res[pstk_i] = i - pstk_i
            stack.append((i,temp))
        return res
