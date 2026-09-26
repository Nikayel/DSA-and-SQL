class Solution:
    def myPow(self, x: float, n: int) -> float:
        #base case : if x == 0: return 0 if n == 0: return 1
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            result = helper(x*x, n//2)
            return x*result if n % 2 == 1 else result
        
        res = helper(x,abs(n))
        if n < 0:
            res = 1 / res
        return res