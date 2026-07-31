class Solution:
    def isHappy(self, n: int) -> bool:  
        while n>=10:
            sm=0
            while n>0:
                dig=n%10
                sm+=dig*dig
                n//=10
            n=sm
        return n==1 or n==7     
                  

        