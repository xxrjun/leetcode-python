# 50. Pow(x, n)
class Solution:

    # Solution 1: Using built in power function
    # myPow = pow

    # Solution 2: Really myPow
    def myPow(self, x: float, n: int) -> float:
            
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n *= - 1
        
        return pow(x ** 2, n / 2) if n % 2 == 0 else x * pow(x ** 2, (n - 1) / 2)




