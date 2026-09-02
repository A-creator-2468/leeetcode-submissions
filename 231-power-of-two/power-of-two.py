class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        for i in range(n+1):
            if n==pow(2,i):
                return True
            if pow(2, i) > n:
                break
    
        return False            
        