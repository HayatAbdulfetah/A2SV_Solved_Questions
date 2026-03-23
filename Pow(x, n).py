class Solution:
    def myPow(self, x: float, n: int) -> float:
        # you can simply return x **n
        # or you can use recursion:
        if n == 1:
            return x
        if n == 0:
            return 1
        x = pow(x,n-1)*x
        
        return x
