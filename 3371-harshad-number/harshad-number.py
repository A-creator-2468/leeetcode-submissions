class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sm=0
        temp=x
        while x>0:
            sm+=x%10
            x//=10
        if temp%sm==0:
            return sm
        return -1
                  
        
        