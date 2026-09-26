class Solution:
    def myPow(self, x: float, n: int) -> float:
        #n = 1
        if n == 1: return x
        #x = 1
        if x == 1: return 1 
        #x = 0
        if x == 0:
            return 0
        #n < 0
        result = 1 # n = 5 x sqr * x sqr * x -> devide // 2 and muliply the reuslt
        power = abs(n)
        while power > 0:
            if power % 2 == 1:
                result *=x
            x*=x
            power = power // 2

        return result if n >= 0 else 1 / result
        
