class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
           #Halve the power
            if x == 1:
                return 1
            if n == 1:
                return x
            if n == 0:
                return 1
            power = abs(n)
            power = power//2
           #recursively call helper on the x*x
            res = helper(x*x, power)
            return res if n%2 == 0 else x*res
           #return helper

        #call helper(x,n)
        res = helper(x,n)
        if n < 0:
            res = 1 / res
        return res
        