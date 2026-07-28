class Solution:
    def climbStairs(self, n: int) -> int:
        #predefine a,b = 1,1
        a,b = 1,1
        for i in range(n):
            temp = a
            a = a+b
            b = temp
        return b